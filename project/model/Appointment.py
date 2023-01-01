from project.model import db


class Appointment(db.Model):
    __tablename__ = "appointment"
    id = db.Column(db.Integer, primary_key=True)
    promocode = db.Column(db.String(255))
    time = db.Column(db.Integer)
    dentist = db.relationship("Dentist", backref="appointment")
    customer = db.relationship("Customer", backref="appointment")
