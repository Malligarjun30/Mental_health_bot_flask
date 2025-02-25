from ChatbotWebsite import create_app

# Create the app
app = create_app()

# Run the app
# if __name__ == '__main__':
#     app.run()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager


# db = SQLAlchemy()
# login_manager = LoginManager()

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db' 
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SECRET_KEY'] = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

#     db.init_app(app)
#     login_manager.init_app(app)

#     with app.app_context():
#         db.create_all()  # Create tables if they don't exist

#     return app

if __name__ == '__main__':
    app.run(debug=True)
