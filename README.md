# 🧘 Ahoum Booking System – Backend API

Backend developer assignment for Ahoum Internship Bootcamp.  
This is a RESTful Flask API for booking sessions & retreats, with:

- JWT-based user authentication
- Event/session listing
- Booking system
- CRM notification via webhook
- PostgreSQL (via Supabase)
- Deployed on Render

---

## 🛠️ Tech Stack

- **Flask** – Lightweight REST API framework
- **SQLAlchemy** – ORM for PostgreSQL
- **PostgreSQL** – Supabase-hosted database
- **JWT** – Secure token-based auth (via `Flask-JWT-Extended`)
- **Gunicorn** – WSGI production server for deployment

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Browse available events/sessions
- ✅ Book events
- ✅ View past & upcoming bookings
- ✅ Notify CRM on booking
- ✅ RESTful API with Postman support

---

## ⚙️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shashipreetham-4/ahoumAI-backend.git
cd ahoum-backend
```

### 2. Create `.env` File

At the root of your project (`/ahoum-backend/`), create a `.env` file with the following content:

```env
DATABASE_URL=your full Supabase URI (URL-encoded password)
JWT_SECRET_KEY=your_super_secure_secret_key
```

> ✅ **Tips**:
>
> - If your password includes special characters like `@`, use **URL-encoded values** (`@` → `%40`)
> - Never commit `.env` to Git — add it to `.gitignore`

### 3. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the App

```bash
python run.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 📘 API Documentation

### 🔐 Authentication

#### POST `/auth/register`

```json
{
  "name": "Shashi",
  "email": "shashi@example.com",
  "password": "secret"
}
```

#### POST `/auth/login`

```json
{
  "email": "shashi@example.com",
  "password": "secret"
}
```

Returns:

```json
{
  "access_token": "<JWT_TOKEN>"
}
```

---

### 📅 Events

#### GET `/events/`

Returns a list of events/sessions.

No auth required.

---

### 📘 Bookings

#### POST `/bookings/`

Headers:

```
Authorization: Bearer <access_token>
```

Body:

```json
{
  "event_id": "<event_id>"
}
```

#### GET `/bookings/mine`

Headers:

```
Authorization: Bearer <access_token>
```

Returns the user’s past and upcoming bookings.

---

## 🛰️ Deployment on Render

### 1. Push to GitHub

Make sure your project is version-controlled and pushed to GitHub.

### 2. Create Render Web Service

- Go to [https://render.com](https://render.com)
- Create a new **Web Service**
- Connect your GitHub repo
- Environment: `Python`
- Build Command:
  ```bash
  pip install -r requirements.txt
  ```
- Start Command:
  ```bash
  gunicorn run:app
  ```

### 3. Add Environment Variables (in Render)

| Key              | Value (from your `.env`)                      |
| ---------------- | --------------------------------------------- |
| `DATABASE_URL`   | your full Supabase URI (URL-encoded password) |
| `JWT_SECRET_KEY` | your JWT secret                               |

Once deployed, your API will be live at:

```
https://your-service-name.onrender.com
```

---

## 📦 Postman Collection

Not required but recommended. You can import this sequence:

1. `POST /auth/register`
2. `POST /auth/login`
3. Use JWT token in headers (`Bearer <token>`)
4. `GET /events/`
5. `POST /bookings/` with `event_id`
6. `GET /bookings/mine`

---

## 💡 Bonus Ideas

- 🔐 Add email verification
- 💰 Integrate Stripe for paid sessions
- 📊 Add facilitator dashboards
- 🔄 Add retry logic for failed CRM notifications

---

## 👨‍💻 Developed by

**Shashi Preetham**  
Backend Developer Internship Assignment – Ahoum  
[LinkedIn](linkedin.com/in/shashi-preetham-cholluri-17760825a)
