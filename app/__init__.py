from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config
from sqlalchemy.pool import QueuePool
from sqlalchemy import event
from sqlalchemy.engine import Engine

# ✅ Use connection pooling to prevent Supabase idle disconnects
db = SQLAlchemy(
    engine_options={
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 10,
        "poolclass": QueuePool,
    }
)

jwt = JWTManager()


# ✅ Safe auto-reconnect logic (no conflict with SQLAlchemy transaction state)
@event.listens_for(Engine, "engine_connect")
def ping_connection(connection, branch):
    if branch:
        return
    try:
        # Use raw DBAPI cursor to ping without starting a transaction
        connection.connection.cursor().execute("SELECT 1")
    except:
        connection.invalidate()
        connection.connection.cursor().execute("SELECT 1")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # ✅ Register Blueprints
    from .routes.auth import auth_bp
    from .routes.events import events_bp
    from .routes.bookings import bookings_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(events_bp, url_prefix="/events")
    app.register_blueprint(bookings_bp, url_prefix="/bookings")

    # ✅ Create all tables
    with app.app_context():
        from . import models

        db.create_all()

    return app
