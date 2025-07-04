from flask import Blueprint, jsonify
from ..models import Event, Facilitator
from .. import db

events_bp = Blueprint("events", __name__)


@events_bp.route("/", methods=["GET"])
def get_all_events():
    events = Event.query.all()
    data = []
    for event in events:
        facilitator = Facilitator.query.get(event.facilitator_id)
        data.append(
            {
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "date": event.date.isoformat(),
                "facilitator": {
                    "id": facilitator.id,
                    "name": facilitator.name,
                    "email": facilitator.email,
                },
            }
        )
    return jsonify(data), 200
