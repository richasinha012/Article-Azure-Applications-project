"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
# TODO: Add any logging levels and handlers with app.logger
# ---------------------------------------------------------
# Configure application logging
logger = logging.getLogger('werkzeug')  # or any name
app.logger.setLevel(logging.INFO)

# Create a handler to output logs to console (Azure reads stdout)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Use a clear log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler only if none exist (prevents duplicate logs)
if not app.logger.handlers:
    app.logger.addHandler(handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
