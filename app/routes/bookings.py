from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import Booking, Event, User, Facilitator
from ..utils.crm_notifier import notify_crm

bookings_bp = Blueprint("bookings", __name__)


# -------- Book Event --------
@bookings_bp.route("/", methods=["POST"])
@jwt_required()
def book_event():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    event_id = data.get("event_id")

    if not event_id:
        return jsonify({"msg": "event_id is required"}), 400

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"msg": "Event not found"}), 404

    booking = Booking(user_id=user_id, event_id=event_id)
    db.session.add(booking)
    db.session.commit()

    notify_crm(user_id=user_id, event=event)
    return jsonify({"msg": "Booking successful"}), 201


# -------- My Bookings --------
@bookings_bp.route("/mine", methods=["GET"])
@jwt_required()
def get_my_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()

    results = []
    for b in bookings:
        event = Event.query.get(b.event_id)
        results.append(
            {
                "booking_id": b.id,
                "event_title": event.title,
                "date": event.date.isoformat(),
            }
        )

    return jsonify(results), 200
