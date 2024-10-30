try:
    from flask import Blueprint, render_template, current_app, request, flash, jsonify
    import uuid
    from .models import db, Pincode, log, Blog
except Exception as e:
    log.error(e)

    

blog = Blueprint('blog', __name__)

# add new blog title and delete
@blog.route('/writterboard', methods=['GET', 'POST'])
def writterboard():
    # print(request.form)
    if request.method == 'POST' and request.form.get('create')=='':
        title = request.form.get('title')
        # print(title)
        language = request.form.get('language')
        u_id = uuid.uuid5(uuid.NAMESPACE_URL, title)
        # print(u_id)
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
    return render_template('blog/writterboard.html', data=data)


@blog.route('/blog-page/<string:blog_id>', methods=['GET', 'POST'])
def blog_page(blog_id):  
    blog_details = Blog.query.filter(Blog.u_id == blog_id).first()
    # print(all_pincode)
    all_pincode = Pincode.query.filter(Pincode.statename == "WEST BENGAL").all()
    # print(all_pincode)
    data = {'blog_details': blog_details, 'all_pincode': all_pincode}
    return render_template('blog/blog-page.html', data=data)

@blog.route('/get-postoffice', methods=[ 'POST'])
def get_postoffice():
    request_data = request.get_json()
    pincode = request_data['pincode']
    data = Pincode.query.with_entities(Pincode.officename).filter(Pincode.pincode == pincode).all()
    # print([office[0] for office in data])
    data = [{'offices': [office[0] for office in data]}]
    # print(data)
    return jsonify(data)


# save or update address
@blog.route('/save-address', methods=[ 'POST'])
def save_address():
    request_data = request.get_json()
    pincode = request_data['pincode']
    office = request_data['postOffice']
    village = request_data['village']
    uid = request_data['uid']
    if '0' in[pincode, office, village, uid]:
        return jsonify({'success': False, 'message': 'All fields are required!'}), 400
    else:
        try:
            selected_blog = Blog.query.filter(Blog.u_id == uid).first()
            selected_blog.blog_pincode = pincode
            selected_blog.blog_postoffice = office
            selected_blog.blog_village = village
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Something went wrong!'}), 500
        else:
            return jsonify({'success': True, 'message': 'Address saved successfully!'}), 200
    


# save content
@blog.route('/submit-content', methods=[ 'POST'])
def save_content():
    request_data = request.get_json()
    # print(request_data)
    content = request_data['content']
    # print(content)
    uid = request_data['uid']
    if '0' in [content, uid]:
        return jsonify({'success': False, 'message': 'All fields are required!'}), 400
    else:
        try:
            selected_blog = Blog.query.filter(Blog.u_id == uid).first()
            selected_blog.body = content
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Something went wrong!'}), 500
        else:
            return jsonify({'success': True, 'message': 'Content saved successfully!'}), 200

