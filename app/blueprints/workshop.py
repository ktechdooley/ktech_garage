from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("workshop", __name__, url_prefix="/workshop")


@bp.route("/")
@login_required
def index():
    return render_template(
        "workshop/index.html",
        title="Workshop",
        subtitle="Workshop",
    )


@bp.route("/jobs")
@login_required
def jobs():
    return render_template(
        "workshop/jobs.html",
        title="Workshop",
        subtitle="Jobs",
    )


@bp.route("/labour-mileage")
@login_required
def labour_mileage():
    return render_template(
        "workshop/labour_mileage.html",
        title="Workshop",
        subtitle="Labour & Mileage",
    )


@bp.route("/service-history")
@login_required
def service_history():
    return render_template(
        "workshop/service_history.html",
        title="Workshop",
        subtitle="Service History",
    )
