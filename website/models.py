try:
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, Numeric, Double, JSON, DateTime, Numeric
    from datetime import datetime
    from .log_setup import setup_logger
except Exception as e:
    print("error in model.py import section", e)


db = SQLAlchemy()
log = setup_logger()

class Blog(db.Model):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    language = Column(String(15))
    u_id = Column(Text)
    title = Column(String(500))
    blog_pincode = Column(Integer)  
    blog_postoffice = Column(String(300))
    blog_village = Column(String(500))
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())
    images = Column(JSON)

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