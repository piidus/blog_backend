import os

DEBUG = True
SECRET_KEY = os.urandom(32)

# database settings
db_user = os.environ.get('DB_USER')
db_user_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')
db_path = os.environ.get('DB_PATH')

# New mail configuration
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD= os.environ.get('MAIL_PWD')
MAIL_PORT = 587
MAIL_SERVER= os.environ.get('MAIL_SERVER')
MAIL_USE_TLS = True
MAIL_USE_SSL = False

# path
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_user_pass}@{db_path}:3306/{db_name}'

# Logging
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'app.log')

# # folder settings
# IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "blog_images/images")

# Folder settings
# Set BASE_DIR to the parent of the project directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# print(BASE_DIR)
IMAGE_FOLDER = os.path.join(BASE_DIR, "blog_images", "images")