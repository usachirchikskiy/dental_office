from project.model import Appointment
from project.schema import  ma, ServiceSchema, DentistSchema

class AppointmentSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    services = ma.Nested(ServiceSchema, many = True)
    dentist = ma.Nested(DentistSchema, many=True)
    class Meta:
        model = Appointment
