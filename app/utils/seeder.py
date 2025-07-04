# app/utils/seeder.py (optional)
from ..models import db, Event, Facilitator
from datetime import datetime


def seed_data():
    if Facilitator.query.first():
        return  # Already seeded

    f1 = Facilitator(name="Alice Coach", email="alice@coach.com")
    f2 = Facilitator(name="Bob Mentor", email="bob@mentor.com")
    db.session.add_all([f1, f2])
    db.session.commit()

    e1 = Event(
        title="Yoga Retreat",
        description="A peaceful 3-day retreat.",
        date=datetime(2025, 8, 10),
        facilitator_id=f1.id,
    )
    e2 = Event(
        title="Mindfulness Workshop",
        description="Learn to be present.",
        date=datetime(2025, 9, 2),
        facilitator_id=f2.id,
    )
    db.session.add_all([e1, e2])
    db.session.commit()
