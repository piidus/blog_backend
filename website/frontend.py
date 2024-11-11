try:
    from flask import Blueprint, render_template, current_app, request, flash, jsonify, send_from_directory
    from .models import log    
except Exception as e:
    log.error(e)

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('frontend/index.html')