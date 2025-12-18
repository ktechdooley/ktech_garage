from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("ecu", __name__, url_prefix="/ecu")


@bp.route("/")
@login_required
def index():
    return render_template(
        "ecu/index.html",
        title="ECU Programming & Calibration",
        subtitle="ECU Programming & Calibration",
    )


@bp.route("/jobs")
@login_required
def ecu_jobs():
    return render_template(
        "ecu/ecu_jobs.html",
        title="ECU Programming & Calibration",
        subtitle="ECU Jobs",
    )


@bp.route("/knowledge-base")
@login_required
def knowledge_base():
    return render_template(
        "ecu/knowledge_base.html",
        title="ECU Programming & Calibration",
        subtitle="ECU Knowledge Base",
    )


@bp.route("/dyno-reports")
@login_required
def dyno_reports():
    return render_template(
        "ecu/dyno_reports.html",
        title="ECU Programming & Calibration",
        subtitle="Dyno Reports",
    )


@bp.route("/file-archive")
@login_required
def file_archive():
    return render_template(
        "ecu/file_archive.html",
        title="ECU Programming & Calibration",
        subtitle="File Archive",
    )
