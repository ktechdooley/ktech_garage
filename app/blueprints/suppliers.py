from flask import Blueprint, render_template

bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")


@bp.route("/suppliers")
def suppliers_list():
    return render_template(
        "suppliers/suppliers.html",
        title="Suppliers",
        subtitle="Suppliers",
    )


@bp.route("/contacts-reps")
def contacts_reps():
    return render_template(
        "suppliers/contacts_reps.html",
        title="Suppliers",
        subtitle="Contacts / Reps",
    )
