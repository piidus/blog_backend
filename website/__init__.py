from flask import Flask
import logging
from .models import db, log 

def create_app():
    #create the object of Flask
    app  = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    app.logger = log
    # Configure Flask's internal logger to only show warnings or higher
    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        db.create_all()


    # register the blueprints
    from  .blog import blog
    app.register_blueprint(blog, url_prefix='/')

    # app.logger.info("Logger has been set up and is writing to %s", app.config['LOG_FILENAME'])

    return app