from flask import Blueprint, render_template

bp = Blueprint("ecu", __name__, url_prefix="/ecu")


@bp.route("/jobs")
def ecu_jobs():
    return render_template(
        "ecu/ecu_jobs.html",
        title="ECU Programming & Calibration",
        subtitle="ECU Jobs",
    )


@bp.route("/knowledge-base")
def ecu_knowledge_base():
    return render_template(
        "ecu/ecu_knowledge_base.html",
        title="ECU Programming & Calibration",
        subtitle="ECU Knowledge Base",
    )


@bp.route("/dyno-reports")
def dyno_reports():
    return render_template(
        "ecu/dyno_reports.html",
        title="ECU Programming & Calibration",
        subtitle="Dyno Reports",
    )


@bp.route("/file-archive")
def file_archive():
    return render_template(
        "ecu/file_archive.html",
        title="ECU Programming & Calibration",
        subtitle="File Archive",
    )
