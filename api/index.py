from flask import Flask
from flask_cors import CORS
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the existing Flask app from src/main.py
try:
    from main import app
except ImportError:
    # If import fails, create a minimal app
    app = Flask(__name__)
    CORS(app, origins="*")
    
    @app.route('/api/health')
    def health():
        return {"status": "OK", "message": "Scripture Search API is running on Vercel"}

# Ensure CORS is enabled
CORS(app, origins="*")

# This is the entry point for Vercel
def handler(event, context):
    return app

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
