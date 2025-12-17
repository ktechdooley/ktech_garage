from flask import Blueprint, render_template

bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@bp.route("/stock-items")
def stock_items():
    return render_template(
        "inventory/stock_items.html",
        title="Inventory & Parts",
        subtitle="Stock Items",
    )


@bp.route("/services")
def services():
    return render_template(
        "inventory/services.html",
        title="Inventory & Parts",
        subtitle="Services",
    )


@bp.route("/price-list")
def price_list():
    return render_template(
        "inventory/price_list.html",
        title="Inventory & Parts",
        subtitle="Price List",
    )
