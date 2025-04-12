from flask import Flask

app = Flask(__name__)

# Import routes or views
from app import routes
