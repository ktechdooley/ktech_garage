from flask import Blueprint, render_template

bp = Blueprint("reports", __name__, url_prefix="/reports")


@bp.route("/")
def vat():
    return render_template(
        "reports/vat.html",
        title="Reports",
        subtitle="VAT",
    )


@bp.route("/profit-loss")
def profit_loss():
    return render_template(
        "reports/profit_loss.html",
        title="Reports",
        subtitle="Profit & Loss",
    )


@bp.route("/ecu-performance-stats")
def ecu_performance_stats():
    return render_template(
        "reports/ecu_performance_stats.html",
        title="Reports",
        subtitle="ECU Performance Stats",
    )
