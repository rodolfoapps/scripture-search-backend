from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

# Simple test data for now
test_scriptures = [
    {
        "id": 1,
        "book": "Matthew",
        "chapter": 6,
        "verse": 3,
        "text": "But when thou doest alms, let not thy left hand know what thy right hand doeth:",
        "collection": "New Testament"
    },
    {
        "id": 2,
        "book": "1 Nephi",
        "chapter": 20,
        "verse": 13,
        "text": "Mine hand hath also laid the foundation of the earth, and my right hand hath spanned the heavens.",
        "collection": "Book of Mormon"
    }
]

@app.route('/api/health')
def health():
    return {"status": "OK", "message": "Scripture Search API is running on Vercel"}

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '').lower()
    
    results = []
    for scripture in test_scriptures:
        if query in scripture['text'].lower():
            results.append(scripture)
    
    return {"results": results, "count": len(results)}

# Vercel handler
def handler(request):
    return app

if __name__ == '__main__':
    app.run(debug=True)
