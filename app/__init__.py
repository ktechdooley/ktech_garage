from flask import Flask
from werkzeug.security import generate_password_hash
import os
from .db import init_db, get_db

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("KTECH_SECRET_KEY", "ktech-change-me")

    os.makedirs("db", exist_ok=True)
    os.makedirs("uploads/ecu", exist_ok=True)
    os.makedirs("uploads/parts", exist_ok=True)

    with app.app_context():
        init_db()
        db = get_db()
        if db.execute("SELECT COUNT(*) c FROM users").fetchone()["c"] == 0:
            db.execute(
                "INSERT INTO users (username,password_hash,role) VALUES (?,?,?)",
                ("admin", generate_password_hash("ktech123"), "admin")
            )
            db.execute("INSERT OR IGNORE INTO settings (id) VALUES (1)")
            db.execute("INSERT OR REPLACE INTO schema_version (id, version) VALUES (1, 1)")
            db.commit()

    # Global template context: business settings
    def inject_business():
        db = get_db()
        s = db.execute("SELECT * FROM settings WHERE id=1").fetchone()
        business = {
            "name": s["business_name"] if s else "kTech Automotive",
            "tagline": s["tagline"] if s else "",
            "location": s["location"] if s else "",
            "phone": s["phone"] if s else "",
            "email": s["email"] if s else "",
        }
        return {"business": business}

    app.context_processor(inject_business)

    from .blueprints.auth import bp as auth_bp
    from .blueprints.main import bp as main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
