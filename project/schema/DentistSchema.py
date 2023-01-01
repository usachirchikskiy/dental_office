from project.model import Dentist
from project.schema import ma


class DentistSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json

    class Meta:
        model = Dentist
