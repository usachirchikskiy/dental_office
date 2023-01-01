from project.model import db


class Service(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    appointment = db.relationship("Appointment", secondary="appointment_service", backref='services')

