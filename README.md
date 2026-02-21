# StoryPulse 📝

A modern blogging platform built with Python and Flask, with a sleek dark UI.

## Features
- User registration, login, and profile management
- Create, update, and delete blog posts
- Password reset via email
- Paginated post feed
- Active authors sidebar

## Local Setup

```bash
# Clone the repo
git clone https://github.com/SaurabhR44/StoryPulse.git
cd StoryPulse

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional - see config.py for defaults)
# SECRET_KEY, EMAIL_USER, EMAIL_PASS

# Run
python run.py
```

Then visit `http://127.0.0.1:5000`.

## Tech Stack
- **Backend**: Flask, SQLAlchemy, Flask-Login, Flask-Mail, Flask-WTF
- **Database**: SQLite (local) / configurable via env var
- **Frontend**: Bootstrap 4, Inter font, custom dark CSS

## Deployment on Vercel
Set the following environment variables in your Vercel project settings:
- `SECRET_KEY` — a long random string
- `SQLALCHEMY_DATABASE_URI` — your production database URL (e.g. PostgreSQL)
- `EMAIL_USER` — Gmail address for password reset emails
- `EMAIL_PASS` — Gmail app password