from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def __repr__(self):
        return f'<User {self.username}>'

class Scripture(db.Model):
    __tablename__ = 'scriptures'
    
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(100), nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    collection = db.Column(db.String(50), nullable=False)  # Old Testament, New Testament, etc.
    
    def to_dict(self):
        return {
            'id': self.id,
            'book': self.book,
            'chapter': self.chapter,
            'verse': self.verse,
            'text': self.text,
            'collection': self.collection,
            'reference': f"{self.book} {self.chapter}:{self.verse}"
        }
    
    def __repr__(self):
        return f'<Scripture {self.book} {self.chapter}:{self.verse}>'