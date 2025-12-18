from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("settings", __name__, url_prefix="/settings")


@bp.route("/")
@login_required
def index():
    return render_template(
        "settings/index.html",
        title="Settings",
        subtitle="Settings",
    )


@bp.route("/business-info")
@login_required
def business_info():
    return render_template(
        "settings/business_info.html",
        title="Settings",
        subtitle="Business Info",
    )


@bp.route("/vat-labour-rates")
@login_required
def vat_labour_rates():
    return render_template(
        "settings/vat_labour_rates.html",
        title="Settings",
        subtitle="VAT & Labour Rates",
    )


@bp.route("/users-security")
@login_required
def users_security():
    return render_template(
        "settings/users_security.html",
        title="Settings",
        subtitle="Users & Security",
    )


@bp.route("/backup-restore")
@login_required
def backup_restore():
    return render_template(
        "settings/backup_restore.html",
        title="Settings",
        subtitle="Backup & Restore",
    )
