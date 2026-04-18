#!/usr/bin/env python
"""
Ohio Trails Explorer - Entry point
Main application logic moved to app.py
"""

from app import create_app
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create and run the Flask app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_ENV', 'development') == 'development')
