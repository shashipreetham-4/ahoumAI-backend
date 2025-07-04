import requests
from ..models import User, Facilitator

CRM_URL = "https://example-crm.com/notify"  # placeholder


def notify_crm(user_id, event):
    user = User.query.get(user_id)
    facilitator = Facilitator.query.get(event.facilitator_id)

    payload = {
        "user": {"id": user.id, "name": user.name, "email": user.email},
        "event": {"id": event.id, "title": event.title, "date": event.date.isoformat()},
        "facilitator_id": facilitator.id,
    }

    try:
        res = requests.post(CRM_URL, json=payload, timeout=5)
        print(f"CRM notified: {res.status_code}")
    except Exception as e:
        print(f"CRM notification failed: {str(e)}")
