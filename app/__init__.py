from flask import Flask
from .routes import frontend_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(frontend_bp)
    return app
