import sys
import os

# Add the project root to the path so imports work correctly
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flaskblog import create_app

app = create_app()

# Vercel expects a callable named 'app' or 'handler'
handler = app
