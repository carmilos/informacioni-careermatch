from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/careermatch')
SECRET_KEY = os.getenv('SECRET_KEY', 'changemepleasegenerateasecret')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '60'))

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'uploads')
