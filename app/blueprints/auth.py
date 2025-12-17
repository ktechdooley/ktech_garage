from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from functools import wraps

from ..db import get_db

bp = Blueprint("auth", __name__)

def login_required(fn):
    @wraps(fn)
    def w(*a, **k):
        if not session.get("user_id"):
            return redirect(url_for("auth.login"))
        return fn(*a, **k)
    return w

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username", "").strip()
        p = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        db = get_db()
        row = db.execute("SELECT * FROM users WHERE username=?", (u,)).fetchone()
        if row and check_password_hash(row["password_hash"], p):
            session.clear()
            session["user_id"] = row["id"]
            session["username"] = row["username"]
            session["role"] = row["role"]
            session.permanent = remember
            return redirect(url_for("main.dashboard"))

        flash("Invalid username or password", "error")

    return render_template("auth/login.html")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
