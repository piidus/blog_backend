from flask import Blueprint, render_template


blog = Blueprint('blog', __name__)

@blog.route('/dashboard')
def dashboard():


    return render_template('blog/dashboard.html')