from ChatbotWebsite import create_app, db

# Create the application context
app = create_app()
with app.app_context():
    db.create_all()
