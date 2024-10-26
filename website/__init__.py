from flask import Flask
import os


def create_app():
    #create the object of Flask
    app  = Flask(__name__)


    # register the blueprints
    from  .blog import blog
    app.register_blueprint(blog, url_prefix='/')

    return app