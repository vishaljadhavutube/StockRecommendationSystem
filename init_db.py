from app import create_app
from app.models.models import db

app = create_app()
with app.app_context():
    db.create_all()
    print("✅ Database initialized.")