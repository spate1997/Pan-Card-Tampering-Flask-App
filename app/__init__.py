from flask import Flask
import os

app = Flask(__name__)

# Set the environment based on the FLASK_ENV variable
env = os.environ.get('FLASK_ENV', 'production')
app.config['ENV'] = env

# Set default configuration
app.config.from_object('config.Config')

# Load environment-specific configuration
if env == "production":
    app.config.from_object('config.ProductionConfig')
elif env == "development":
    app.config.from_object('config.DevelopmentConfig')
elif env == "testing":
    app.config.from_object('config.TestingConfig')
elif env == "debug":
    app.config.from_object('config.DebugConfig')

from app import views
