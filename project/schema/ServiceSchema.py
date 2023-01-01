from project.model import Service
from project.schema import ma

class ServiceSchema(ma.SQLAlchemyAutoSchema): # convert DB object to Json

    class Meta:
        model = Service