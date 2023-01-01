from flask_marshmallow import Marshmallow
ma = Marshmallow()


from project.schema.CustomerSchema import CustomerSchema
from project.schema.DentistSchema import DentistSchema
from project.schema.ServiceSchema import ServiceSchema
from project.schema.AppointmentSchema import AppointmentSchema

def init_app(app):
    ma.init_app(app)