import sqlite3
from flask import g
from pathlib import Path

DB_PATH = Path("db/ktech.db")

def get_db():
    if "db" not in g:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        g.db = conn
    return g.db

def init_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON;")
    schema = Path("db/schema.sql").read_text(encoding="utf-8")
    db.executescript(schema)
    db.execute("INSERT OR IGNORE INTO settings (id) VALUES (1)")
    db.execute("INSERT OR IGNORE INTO schema_version (id, version) VALUES (1, 1)")
    db.commit()
    db.close()
