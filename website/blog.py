try:
    from flask import Blueprint, render_template, current_app, request, flash
    import uuid
    from .models import db, Pincode, log, Blog
except Exception as e:
    log.error(e)

    

blog = Blueprint('blog', __name__)

# add new blog title and delete
@blog.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST' and request.form.get('create'):
        title = request.form.get('title')
        language = request.form.get('language')
        u_id = uuid.uuid5(uuid.NAMESPACE_URL, title)
        try:
            blog = Blog(title=title, language=language, u_id=u_id)        
            db.session.add(blog)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash('Something went wrong!', 'danger')
        else:
            flash('Blog Title created successfully!', 'success')
    
    # delete a post
    if request.method == 'POST' and request.form.get('delete'):
        id = request.form.get('delete')
        try:
            blog = Blog.query.get(id)
            db.session.delete(blog)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash('Something went wrong!', 'danger')
        else:
            flash('Blog Title deleted successfully!', 'success')


   
    try:
        data = Blog.query.all()
    except Exception as e:
        data = []
    return render_template('blog/dashboard.html', data=data)


@blog.route('/blog-page/<string:blog_id>', methods=['GET', 'POST'])
def blog_page(blog_id):  
    blog_details = Blog.query.filter(Blog.u_id == blog_id).first()
    # print(all_pincode)
    all_pincode = Pincode.query.filter(Pincode.statename == "WEST BENGAL").all()
    print(all_pincode)
    data = {'blog_details': blog_details, 'all_pincode': all_pincode}
    return render_template('blog/blog-page.html', data=data)

