from .CustomerRoute import customer_bp


def init_app(app):
    app.register_blueprint(customer_bp)