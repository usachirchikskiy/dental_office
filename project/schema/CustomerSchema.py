from project.model import Customer
from project.schema import ma


class CustomerSchema(ma.SQLAlchemyAutoSchema): # convert DB object to Json

    class Meta:
        model = Customer