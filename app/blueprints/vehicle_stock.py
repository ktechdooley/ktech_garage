from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("vehicle_stock", __name__, url_prefix="/vehicle-stock")


@bp.route("/")
@login_required
def index():
    return render_template(
        "vehicle_stock/index.html",
        title="Vehicle Stock",
        subtitle="Vehicle Stock",
    )


@bp.route("/stock-vehicles")
@login_required
def stock_vehicles():
    return render_template(
        "vehicle_stock/stock_vehicles.html",
        title="Vehicle Stock",
        subtitle="Stock Vehicles",
    )


@bp.route("/prep-jobs")
@login_required
def prep_jobs():
    return render_template(
        "vehicle_stock/prep_jobs.html",
        title="Vehicle Stock",
        subtitle="Prep Jobs",
    )


@bp.route("/external-costs")
@login_required
def external_costs():
    return render_template(
        "vehicle_stock/external_costs.html",
        title="Vehicle Stock",
        subtitle="External Costs",
    )


@bp.route("/profit-analysis")
@login_required
def profit_analysis():
    return render_template(
        "vehicle_stock/profit_analysis.html",
        title="Vehicle Stock",
        subtitle="Profit Analysis",
    )
