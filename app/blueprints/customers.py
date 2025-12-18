from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.route("/")
@login_required
def index():
    return render_template(
        "customers/index.html",
        title="Customers",
        subtitle="Customers",
    )


@bp.route("/vehicles")
@login_required
def vehicles():
    return render_template(
        "customers/vehicles.html",
        title="Customers",
        subtitle="Vehicles",
    )


@bp.route("/vehicle-history")
@login_required
def vehicle_history():
    return render_template(
        "customers/vehicle_history.html",
        title="Customers",
        subtitle="Vehicle History",
    )
