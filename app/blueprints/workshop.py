from flask import Blueprint, render_template

bp = Blueprint("workshop", __name__, url_prefix="/workshop")


@bp.route("/jobs")
def jobs():
    return render_template(
        "workshop/jobs.html",
        title="Workshop",
        subtitle="Jobs",
    )


@bp.route("/labour-mileage")
def labour_mileage():
    return render_template(
        "workshop/labour_mileage.html",
        title="Workshop",
        subtitle="Labour & Mileage",
    )


@bp.route("/service-history")
def service_history():
    return render_template(
        "workshop/service_history.html",
        title="Workshop",
        subtitle="Service History",
    )
