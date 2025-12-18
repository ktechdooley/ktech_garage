from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("invoicing", __name__, url_prefix="/invoicing")


@bp.route("/")
@login_required
def index():
    return render_template(
        "invoicing/index.html",
        title="Invoicing",
        subtitle="Invoicing",
    )


@bp.route("/sales-invoices")
@login_required
def sales_invoices():
    return render_template(
        "invoicing/sales_invoices.html",
        title="Invoicing",
        subtitle="Sales Invoices (Money In)",
    )


@bp.route("/purchase-invoices")
@login_required
def purchase_invoices():
    return render_template(
        "invoicing/purchase_invoices.html",
        title="Invoicing",
        subtitle="Purchase Invoices (Money Out)",
    )
