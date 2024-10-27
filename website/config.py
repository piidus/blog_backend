import os

DEBUG = True
SECRET_KEY = os.urandom(32)

# database settings
db_user = os.environ.get('DB_USER')
db_user_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')
db_path = os.environ.get('DB_PATH')

# path
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_user_pass}@{db_path}:3306/{db_name}'

# Logging
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'app.log')