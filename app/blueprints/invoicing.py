from flask import Blueprint, render_template

bp = Blueprint("invoicing", __name__, url_prefix="/invoicing")


@bp.route("/sales-invoices")
def sales_invoices():
    return render_template(
        "invoicing/sales_invoices.html",
        title="Invoicing",
        subtitle="Sales Invoices (Money In)",
    )


@bp.route("/purchase-invoices")
def purchase_invoices():
    return render_template(
        "invoicing/purchase_invoices.html",
        title="Invoicing",
        subtitle="Purchase Invoices (Money Out)",
    )
