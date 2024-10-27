from flask import Flask
import os
from .models import db
from .log_setup import setup_logger

def create_app():
    #create the object of Flask
    app  = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    # set logger
    setup_logger(app)

    with app.app_context():
        db.create_all()


    # register the blueprints
    from  .blog import blog
    app.register_blueprint(blog, url_prefix='/')

    return app