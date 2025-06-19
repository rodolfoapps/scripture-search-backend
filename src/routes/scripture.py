from flask import Blueprint, jsonify, request
from src.models.user import Scripture, db
from sqlalchemy import or_, and_
import re

scripture_bp = Blueprint('scripture', __name__)

@scripture_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'message': 'Scripture Search API is running',
        'timestamp': str(db.func.now())
    })

@scripture_bp.route('/search', methods=['POST'])
def search_scriptures():
    """Search scriptures with filtering options"""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        collections = data.get('collections', [])
        books = data.get('books', [])
        limit = data.get('limit', 1000)
        
        if not query:
            return jsonify({'error': 'Query parameter is required'}), 400
        
        # Start with base query
        search_query = Scripture.query
        
        # Apply collection filters
        if collections:
            search_query = search_query.filter(Scripture.collection.in_(collections))
        
        # Apply book filters
        if books:
            search_query = search_query.filter(Scripture.book.in_(books))
        
        # Split query into words for multiple word search
        words = [word.strip() for word in query.split() if word.strip()]
        
        # Create search conditions for each word
        search_conditions = []
        for word in words:
            search_conditions.append(Scripture.text.ilike(f'%{word}%'))
        
        # Apply search conditions (all words must be present)
        if search_conditions:
            search_query = search_query.filter(and_(*search_conditions))
        
        # Execute query with limit
        results = search_query.limit(limit).all()
        
        # Highlight search terms in results
        highlighted_results = []
        for scripture in results:
            scripture_dict = scripture.to_dict()
            highlighted_text = highlight_search_terms(scripture.text, words)
            scripture_dict['highlighted_text'] = highlighted_text
            highlighted_results.append(scripture_dict)
        
        return jsonify({
            'results': highlighted_results,
            'count': len(highlighted_results),
            'query': query,
            'filters': {
                'collections': collections,
                'books': books
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@scripture_bp.route('/collections', methods=['GET'])
def get_collections():
    """Get all available scripture collections"""
    collections = [
        'Old Testament',
        'New Testament', 
        'Book of Mormon',
        'Doctrine and Covenants',
        'Pearl of Great Price'
    ]
    return jsonify({'collections': collections})

@scripture_bp.route('/books', methods=['GET'])
def get_books():
    """Get all books organized by collection"""
    books_by_collection = {
        'Old Testament': [
            'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
            'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel',
            '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra',
            'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs',
            'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations',
            'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos',
            'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk',
            'Zephaniah', 'Haggai', 'Zechariah', 'Malachi'
        ],
        'New Testament': [
            'Matthew', 'Mark', 'Luke', 'John', 'Acts',
            'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians',
            'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy',
            '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James',
            '1 Peter', '2 Peter', '1 John', '2 John', '3 John',
            'Jude', 'Revelation'
        ],
        'Book of Mormon': [
            '1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom',
            'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman',
            '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni'
        ],
        'Doctrine and Covenants': [
            'Doctrine and Covenants'  # Treat as single book, not individual sections
        ],
        'Pearl of Great Price': [
            'Moses', 'Abraham', 'Joseph Smith—Matthew', 'Joseph Smith—History', 'Articles of Faith'
        ]
    }
    return jsonify({'books': books_by_collection})

@scripture_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get database statistics"""
    total_verses = Scripture.query.count()
    collections_count = db.session.query(Scripture.collection).distinct().count()
    books_count = db.session.query(Scripture.book).distinct().count()
    
    return jsonify({
        'total_verses': total_verses,
        'collections': collections_count,
        'books': books_count
    })

def highlight_search_terms(text, search_terms):
    """Highlight search terms in text with HTML markup"""
    highlighted_text = text
    
    for term in search_terms:
        # Use case-insensitive replacement with word boundaries
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        highlighted_text = pattern.sub(
            lambda m: f'<mark style="background-color: yellow; font-weight: bold;">{m.group()}</mark>',
            highlighted_text
        )
    
    return highlighted_text

