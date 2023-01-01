from flask import jsonify, request, Blueprint

from project.model import Customer, db, Dentist, Service, ServiceAppointmentCrossRef, Appointment
from project.schema import AppointmentSchema, ServiceSchema

customer_bp = Blueprint('customer_bp', __name__)
app_schema = AppointmentSchema()
service_schema = ServiceSchema()

@customer_bp.route("/addService", methods=["POST"])
def add_service():
    body = request.get_json()
    name = body['name']
    price = body['price']
    service = Service()
    service.name = name
    service.price = price
    db.session.add(service)
    db.session.commit()
    return jsonify(
        message="service added"
    )

@customer_bp.route("/addCustomer", methods=["POST"])
def add_customer():
    body = request.get_json()
    name = body['name']
    photo = body['photo']
    number = body["number"]
    customer = Customer()
    customer.name = name
    customer.photo = photo
    customer.number = number
    db.session.add(customer)
    db.session.commit()
    return jsonify(
        message="customer added"
    )


@customer_bp.route("/updateCustomer/<int:id>", methods=["POST"])
def update_customer(id):
    body = request.get_json()
    app_id = body["app_id"]
    customer = Customer.get(id)
    customer.appointment_id = app_id
    db.session.commit()
    return jsonify(
        message="customer updated"
    )


@customer_bp.route("/addDentist", methods=["POST"])
def add_dentist():
    body = request.get_json()
    name = body['name']
    photo = body['photo']
    number = body["number"]
    dentist = Dentist()
    dentist.name = name
    dentist.photo = photo
    dentist.number = number
    db.session.add(dentist)
    db.session.commit()
    return jsonify(
        message="dentist added"
    )


@customer_bp.route("/updateDentist/<int:id>", methods=["POST"])
def update_dentist(id):
    body = request.get_json()
    app_id = body["app_id"]
    dentist = Dentist.query.get(id)
    dentist.appointment_id = app_id
    db.session.commit()
    return jsonify(
        message="dentist updated"
    )


@customer_bp.route("/addServiceAppCrossRef", methods=["POST"])
def add_service_appointment_crossRef():
    body = request.get_json()
    service_id = body['service_id']
    app_id = body['app_id']
    crossRef = ServiceAppointmentCrossRef()
    crossRef.service_id =service_id
    crossRef.appointment_id = app_id
    service = Service.query.get(service_id)
    appointment = Appointment.query.get(app_id)
    service.appointment.append(appointment)
    print(service.appointment)
    print(appointment.service)
    db.session.add(crossRef)
    db.session.commit()
    return jsonify(
        message="crossRef added"
    )

@customer_bp.route("/addAppointment", methods=["POST"])
def add_appointment():
    body = request.get_json()
    promococde = body['promocode']
    time = body['time']
    appointment = Appointment()
    appointment.promocode =promococde
    appointment.time = time
    db.session.add(appointment)
    db.session.commit()
    return jsonify(
        message="appointment added"
    )

@customer_bp.route("/getService/<int:id>", methods=["GET"])
def get_service(id):
    service = Service.query.get(id)
    return jsonify(service_schema.dump(service))

@customer_bp.route("/getAppointment/<int:id>", methods=["GET"])
def get_appointment(id):
    appointment = Appointment.query.get(id)
    return jsonify(app_schema.dump(appointment))