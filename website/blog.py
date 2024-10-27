try:
    from flask import Blueprint, render_template, current_app
    from .models import db, Pincode, log
except Exception as e:
    log.error(e)
else:
    log.info("model imported")
    

blog = Blueprint('blog', __name__)


@blog.route('/dashboard')
def dashboard():
   

   
    current_app.logger.info("info message")
    data = []
    return render_template('blog/dashboard.html', data=data)


@blog.route('/blog-page/<string:blog_id>', methods=['GET', 'POST'])
def blog_page(**kwargs):  
    blog_id = kwargs['blog_id']  
    if blog_id is None:
        all_pincode = Pincode.query.filter(Pincode.pincode == 700135).all()
    # print(all_pincode)
    
    data = {'pincode':all_pincode}
    return render_template('blog/blog-page.html', data=data)

