from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@bp.route("/")
@login_required
def index():
    return render_template(
        "inventory/index.html",
        title="Inventory & Parts",
        subtitle="Inventory & Parts",
    )


@bp.route("/stock-items")
@login_required
def stock_items():
    return render_template(
        "inventory/stock_items.html",
        title="Inventory & Parts",
        subtitle="Stock Items",
    )


@bp.route("/services")
@login_required
def services():
    return render_template(
        "inventory/services.html",
        title="Inventory & Parts",
        subtitle="Services",
    )


@bp.route("/price-list")
@login_required
def price_list():
    return render_template(
        "inventory/price_list.html",
        title="Inventory & Parts",
        subtitle="Price List",
    )
