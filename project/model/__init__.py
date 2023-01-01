from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from project.model.Dentist import Dentist
from project.model.ServiceAppointmentCrossRef import ServiceAppointmentCrossRef
from project.model.Service import Service
from project.model.Customer import Customer
from project.model.Appointment import Appointment

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
