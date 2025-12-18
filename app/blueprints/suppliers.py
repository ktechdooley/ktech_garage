from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")


@bp.route("/")
@login_required
def index():
    return render_template(
        "suppliers/index.html",
        title="Suppliers",
        subtitle="Suppliers",
    )


@bp.route("/contacts-reps")
@login_required
def contacts_reps():
    return render_template(
        "suppliers/contacts_reps.html",
        title="Suppliers",
        subtitle="Contacts / Reps",
    )
