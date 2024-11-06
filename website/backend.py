
try:
    from flask import Blueprint, render_template, current_app, request, flash, jsonify, send_from_directory
    import uuid, os, json
    from werkzeug.utils import secure_filename
    from .models import db, Pincode, log, Blog
except Exception as e:
    log.error(e)

    

backend = Blueprint('backend', __name__)

# add new blog title and delete
@backend.route('/writterboard', methods=['GET', 'POST'])
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

# serve image
# Route to serve images from the external directory
@backend.route('/blog_images/<path:filename>')
def blog_images(filename):
    return send_from_directory(current_app.config['IMAGE_FOLDER'], filename)
# save image    
@backend.route('/save-image', methods=['POST'])
def save_image():
    if request.method == 'POST':  
        request_data = request.files['image'] 
        blog_id = request.form.get('uid')
        blog = Blog.query.filter(Blog.u_id == blog_id).first()
        # convert image to as path
        url_path = os.path.join(current_app.config['IMAGE_FOLDER'], secure_filename(request_data.filename)).replace('\\', '/')
    #    save image
        # save to image folder
        request_data.save(os.path.join(current_app.config['IMAGE_FOLDER'], secure_filename(request_data.filename)))
        # image name save as json
        # check if any image exists then get the image serial no and add 1
        if blog.images:
            images = blog.images
            existing_json = json.loads(blog.images)
            
            # print(images)
            if len(images) > 0:
                last_key = [key for key in existing_json.keys()][-1]
                serial_no = int(last_key) + 1
                existing_json.update({str(serial_no): url_path})
            else:
                serial_no = 1
                existing_json = {str(serial_no): url_path}
        else:
            serial_no = 1
            existing_json = {str(serial_no): url_path}
        # save as json            
        try:
            blog.images = json.dumps(existing_json)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Something went wrong!'}), 500
        # print(request_data)
        
        return jsonify({'success': True, 'message': 'Image saved successfully!'}), 200

@backend.route('/blog-page/<string:blog_id>', methods=['GET', 'POST'])
def blog_page(blog_id):  
    blog_details = Blog.query.filter(Blog.u_id == blog_id).first()
    # print(all_pincode)
    all_pincode = Pincode.query.filter(Pincode.statename == "WEST BENGAL").all()
    # print(all_pincode)
    # images list
    if blog_details.images:
        images = json.loads(blog_details.images)
        for key, value in images.items():
            print(key, value)
        image_urls = [value.split('/')[-1] for key, value in images.items()]
    else:
        image_urls = []  # Collect all image URLs
    data = {'blog_details': blog_details, 'all_pincode': all_pincode, 'image_urls': image_urls}
    return render_template('blog/blog-writer.html', data=data)

@backend.route('/get-postoffice', methods=[ 'POST'])
def get_postoffice():
    # print(request.get_json())
    request_data = request.get_json()
    pincode = request_data['pincode']
    data = Pincode.query.with_entities(Pincode.officename).filter(Pincode.pincode == pincode).all()
    # print([office[0] for office in data])
    data = [{'offices': [office[0] for office in data]}]
    # print(data)
    return jsonify(data)


# save or update address
@backend.route('/save-address', methods=[ 'POST'])
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
@backend.route('/submit-content', methods=[ 'POST'])
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

