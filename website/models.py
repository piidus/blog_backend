try:
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, Numeric, Double, JSON, DateTime, Numeric
except Exception as e:
    print("error in model.py import section", e)

db = SQLAlchemy()

# pincode model
'''
'officename', 'pincode', 'officetype', 'deliverystatus', 'divisionname',
       'regionname', 'circlename', 'taluk', 'districtname', 'statename',
       'telephone', 'related_suboffice', 'related_headoffice', 'longitude',
       'latitude' '''
class Pincode(db.Model):
    __tablename__ = 'pincode'
    id = Column(Integer, primary_key=True)
    pincode = Column(Integer)
    officename = Column(String)
    officetype = Column(String)
    deliverystatus = Column(String)
    divisionname = Column(String)
    regionname = Column(String)
    circlename = Column(String)
    taluk = Column(String)
    districtname = Column(String)
    statename = Column(String)
    telephone = Column(String)
    related_suboffice = Column(String)
    related_headoffice = Column(String)
    longitude = Column(String)
    latitude = Column(String)