from project.model import db


class ServiceAppointmentCrossRef(db.Model):
    __tablename__ = "appointment_service"
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointment.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))