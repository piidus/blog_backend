from flask import Flask, render_template
import logging, os
from flask_login import LoginManager
from .models import db, log, User, mail

def create_app():
    #create the object of Flask
    app  = Flask(__name__)
    app.config.from_pyfile('config.py')
    mail.init_app(app)
    
    try:
        db.init_app(app)
    except Exception as e:
        log.error(e)
    app.logger = log
    # Configure Flask's internal logger to only show warnings or higher
    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        db.create_all()


    # register the blueprints
    from  .backend import backend
    app.register_blueprint(backend, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .frontend import frontend
    app.register_blueprint(frontend, url_prefix='/')

    # app.logger.info("Logger has been set up and is writing to %s", app.config['LOG_FILENAME'])

    # Initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Custom 404 error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    # # make folders in root
    # IMAGE_FOLDER = app.config['IMAGE_FOLDER']   
    # os.makedirs(os.path.join(IMAGE_FOLDER), exist_ok=True)
    # Create the folder if it doesn't exist
    image_folder_path = app.config['IMAGE_FOLDER']
    os.makedirs(image_folder_path, exist_ok=True)
    return app