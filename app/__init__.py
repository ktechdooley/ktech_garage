from flask import Flask
from .db import init_app


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    init_app(app)

    from .blueprints import (
        auth,
        main,
        customers,
        workshop,
        ecu,
        vehicle_stock,
        inventory,
        invoicing,
        suppliers,
        reports,
        settings,
    )

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(customers.bp)
    app.register_blueprint(workshop.bp)
    app.register_blueprint(ecu.bp)
    app.register_blueprint(vehicle_stock.bp)
    app.register_blueprint(inventory.bp)
    app.register_blueprint(invoicing.bp)
    app.register_blueprint(suppliers.bp)
    app.register_blueprint(reports.bp)
    app.register_blueprint(settings.bp)

    app.add_url_rule("/", endpoint="main.dashboard")

    return app
