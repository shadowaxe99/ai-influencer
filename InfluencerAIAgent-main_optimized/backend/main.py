import os
from flask import Flask, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from celery import Celery
from sqlalchemy_utils import database_exists, create_database, drop_database
from dotenv import load_dotenv
from passlib.hash import sha256_crypt
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
import logging
import sys
from agents import BrandCollaboration, manageContacts, scheduleAppointments, PRMediaAgent, designUIUX, \
    measureUserEngagement, collectUserFeedback, countActiveUsers, countBrandCollaborations, Agent1, Agent2, Agent3

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
app.config['DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "app.db")}'
app.config['TESTING'] = bool(int(os.environ.get('TESTING', 0)))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not database_exists(app.config['DATABASE_URI']):
    create_database(app.config['DATABASE_URI'])

db = SQLAlchemy(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

if app.config['TESTING']:
    db.create_all()

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_hashed_password(plain_text_password):
    return sha256_crypt.encrypt(plain_text_password)

def check_password(plain_text_password, hashed_password):
    return sha256_crypt.verify(plain_text_password, hashed_password)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password(password, user.password):
        return True
    else:
        return False

def generate_token(user_id):
    payload = {'user_id': user_id}
    secret = current_app.config.get('SECRET_KEY').encode('utf-8')
    token = encode(payload, secret, algorithm='HS256')
    return token

def parse_token(token):
    try:
        secret = current_app.config.get('SECRET_KEY').encode('utf-8')
        decoded = decode(token, secret, algorithms=['HS256'])
        return decoded['user_id']
    except (ExpiredSignatureError, InvalidTokenError):
        raise AuthException("Invalid or expired token.")

class AuthException(Exception):
    pass

@app.before_first_request
def initialize_db():
    if not database_exists(app.config['DATABASE_URI']):
        create_database(app.config['DATABASE_URI'])
        db.create_all()

@app.route("/login", methods=["POST"])
def login():
    credentials = request.get_json()
    if authenticate(credentials.get("username"), credentials.get("password")):
        token = generate_token(1)
        return jsonify({'auth_token': token.decode('utf-8')})
    else:
        raise AuthException("Invalid username or password.")

# Add routes for different agents here by calling their respective methods
# Similar to the provided examples for Agents 1, 2, and 3.

@app.errorhandler(AuthException)
def auth_exception_handler(err):
    response = {"error": str(err)}
    return jsonify(response), 401

def create_app():
    # Configure this function properly to support blueprints and configurations
    pass

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
