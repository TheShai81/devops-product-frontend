from flask import Flask

app = Flask(__name__)

# Import routes AFTER app is created to avoid circular imports
from app import routes