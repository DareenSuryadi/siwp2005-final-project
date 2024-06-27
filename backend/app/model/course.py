from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    description = db.StringField(required=False)
    
class Bulletin(db.Document):
    name = db.StringField(required=True)
    content =  db.StringField(required=False)
    # course = db.ReferenceField(Course)

class Billing(db.Document):
    name = db.StringField(required=True)
    nim = db.StringField(required=True)
    billing = db.StringField(required=True)
    semester = db.StringField(required=True)

class Academic(db.Document):
    name = db.StringField(required=True)
    nim = db.StringField(required=True)
    course = db.StringField(required=True)
    type = db.StringField(required=True)
    semester = db.StringField(required=True)
    grade = db.StringField(required=True)

class Softskill(db.Document):
    name = db.StringField(required=True)
    nim = db.StringField(required=True)
    title = db.StringField(required=True)
    organizer = db.StringField(required=True)
    year = db.StringField(required=True)
    content = db.StringField(required=True)