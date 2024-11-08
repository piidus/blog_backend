try:
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import Column, Integer, String, Boolean, Text, JSON, DateTime, ForeignKey
    from sqlalchemy.orm import relationship
    from datetime import datetime
    from flask_login import UserMixin
    from flask_mail import Mail
    from .log_setup import setup_logger
except Exception as e:
    print("error in model.py import section", e)


db = SQLAlchemy()
log = setup_logger()
mail = Mail()

# Association table for many-to-many relationship between Blog and Tag
tags = db.Table('tags',
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
    Column('blog_id', Integer, ForeignKey('blog.id'), primary_key=True)
)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    
    # Relationship to blogs
    blogs = relationship('Blog', secondary=tags, back_populates='tags')
class Blog(db.Model):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    language = Column(String(15))
    u_id = Column(Text)
    title = Column(String(500))
    blog_pincode = Column(Integer)  
    blog_postoffice = Column(String(300))
    blog_village = Column(String(500))
    blog_district = Column(String(500))
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())
    images = Column(JSON)

    # Relationship to tags
    tags = relationship('Tag', secondary=tags, back_populates='blogs')
    
class Pincode(db.Model):
    __tablename__ = 'pincode'
    id = Column(Integer, primary_key=True)
    pincode = Column(Integer)
    officename = Column(String(300))
    officetype = Column(String(300))
    deliverystatus = Column(String(300))
    divisionname = Column(String(300))
    regionname = Column(String(300))
    circlename = Column(String(300))
    taluk = Column(String(300))
    districtname = Column(String(300))
    statename = Column(String(300))
    telephone = Column(String(300))
    related_suboffice = Column(String(300))
    related_headoffice = Column(String(300))
    longitude = Column(String(300))
    latitude = Column(String(300))




# user model
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(210))
    first_name = Column(String(150))
    last_name = Column(String(150))
    phone = Column(String(13))
    role = Column(String(10), default= 'user', nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    active = Column(Boolean(), default= True)





