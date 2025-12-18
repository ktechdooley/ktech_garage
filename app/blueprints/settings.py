from flask import Blueprint, render_template

bp = Blueprint("settings", __name__, url_prefix="/settings")


@bp.route("/")
def business_info():
    return render_template(
        "settings/business_info.html",
        title="Settings",
        subtitle="Business Info",
    )


@bp.route("/vat-labour-rates")
def vat_labour_rates():
    return render_template(
        "settings/vat_labour_rates.html",
        title="Settings",
        subtitle="VAT & Labour Rates",
    )


@bp.route("/users-security")
def users_security():
    return render_template(
        "settings/users_security.html",
        title="Settings",
        subtitle="Users & Security",
    )


@bp.route("/backup-restore")
def backup_restore():
    return render_template(
        "settings/backup_restore.html",
        title="Settings",
        subtitle="Backup & Restore",
    )
