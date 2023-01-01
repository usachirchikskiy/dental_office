from project.model import db


class Dentist(db.Model):
    __tablename__ = "dentist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    number = db.Column(db.String(255))
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointment.id"))