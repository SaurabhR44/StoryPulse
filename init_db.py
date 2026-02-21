import sys
import os

# Add the current directory to the sys.path
sys.path.append(os.getcwd())

from flaskblog import create_app, db
from flaskblog.models import User, Post

def init_database():
    print("🚀 Initializing database...")
    
    # Check if SQLALCHEMY_DATABASE_URI is set to a production database
    db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    if not db_uri or 'sqlite' in db_uri:
        print("⚠️  Warning: SQLALCHEMY_DATABASE_URI is not set or is using SQLite.")
        print("If you are deploying to Vercel, make sure to set this environment variable to a PostgreSQL URL.")
        confirm = input("Do you want to continue with the current setting? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Aborted.")
            return

    app = create_app()
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"❌ Error creating database: {e}")

if __name__ == "__main__":
    init_database()
