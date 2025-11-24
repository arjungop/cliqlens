"""
Vercel serverless entry point for CliqLens
Imports the Flask app from the parent directory
"""

import sys
import os

# Add parent directory to Python path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

# Vercel expects a variable called 'app' or 'application'
# Flask app is already named 'app', so it will work directly
