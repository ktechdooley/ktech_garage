from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("reports", __name__, url_prefix="/reports")


@bp.route("/")
@login_required
def index():
    return render_template(
        "reports/index.html",
        title="Reports",
        subtitle="Reports",
    )


@bp.route("/vat")
@login_required
def vat():
    return render_template(
        "reports/vat.html",
        title="Reports",
        subtitle="VAT",
    )


@bp.route("/profit-loss")
@login_required
def profit_loss():
    return render_template(
        "reports/profit_loss.html",
        title="Reports",
        subtitle="Profit & Loss",
    )


@bp.route("/ecu-performance-stats")
@login_required
def ecu_performance_stats():
    return render_template(
        "reports/ecu_performance_stats.html",
        title="Reports",
        subtitle="ECU Performance Stats",
    )
