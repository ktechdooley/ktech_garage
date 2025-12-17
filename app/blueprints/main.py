from flask import Blueprint, render_template, request, redirect, url_for, flash
from .auth import login_required

bp = Blueprint("main", __name__)

@bp.route("/")
@login_required
def dashboard():
    return render_template("main/dashboard.html")


@bp.route('/quick_search')
@login_required
def quick_search():
    q = (request.args.get('q') or '').strip()
    if not q:
        return redirect(url_for('main.dashboard'))
    flash(f"Quick search for '{q}' will be enabled when the Vehicles module is wired in.", "info")
    return redirect(url_for('main.dashboard'))
