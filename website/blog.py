from flask import Blueprint, render_template
from .models import db, Pincode
from flask import current_app

blog = Blueprint('blog', __name__)


@blog.route('/dashboard')
def dashboard():
    # get all pincode from database
    all_pincode = Pincode.query.filter(Pincode.pincode == 700135).all()
    # print(all_pincode)
    data = []
    data = {'pincode':all_pincode}


   
    current_app.logger.info("info message")
    current_app.logger.warning("warning message")
    current_app.logger.error("error message")

    return render_template('blog/dashboard.html', data=data)