from flask import Blueprint, render_template

bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.route("/")
def customers_list():
    return render_template(
        "customers/customers.html",
        title="Customers",
        subtitle="Customers",
    )


@bp.route("/vehicles")
def vehicles():
    return render_template(
        "customers/vehicles.html",
        title="Customers",
        subtitle="Vehicles",
    )


@bp.route("/vehicle-history")
def vehicle_history():
    return render_template(
        "customers/vehicle_history.html",
        title="Customers",
        subtitle="Vehicle History",
    )
