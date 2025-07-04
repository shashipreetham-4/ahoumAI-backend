import uuid
from datetime import datetime
from . import db


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    bookings = db.relationship("Booking", backref="user", lazy=True)


class Facilitator(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    events = db.relationship("Event", backref="facilitator", lazy=True)


class Event(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    facilitator_id = db.Column(
        db.String, db.ForeignKey("facilitator.id"), nullable=False
    )

    bookings = db.relationship("Booking", backref="event", lazy=True)


class Booking(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
    event_id = db.Column(db.String, db.ForeignKey("event.id"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
