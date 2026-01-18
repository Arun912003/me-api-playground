🚀 Project Overview

Me API Playground is a backend-focused application that exposes REST APIs to serve personal profile data and perform skill-based project queries. The system is designed with an API-first approach and includes a minimal frontend for demonstration.

This project fulfills all requirements of the backend assessment, including health checks, data modeling, querying, and a working UI.

🧱 Tech Stack

Backend: Django, Django REST Framework

Database: SQLite

Frontend: HTML, JavaScript (Fetch API)

Tools: VS Code, Git

📂 Project Structure
me-api-playground/
│── me_api/           # Django project settings
│── profileapi/       # Core app (models, views, APIs)
│── frontend/         # Simple HTML frontend
│── db.sqlite3        # Database
│── manage.py
│── requirements.txt

🗃️ Database Schema
Profile

name (string)

email (string)

education (string)

skills (JSON array)

github (URL)

linkedin (URL)

portfolio (URL)

Project

title (string)

description (string)

links (JSON)

profile (Foreign Key)

🔗 API Endpoints
Health Check
GET /api/health/


Response

{ "status": "ok" }

Get Profile
GET /api/profile/


Returns full profile details including projects.

Create Profile
POST /api/profile/

Search Projects by Skill
GET /api/projects?skill=Python


Response

[
  "Planora AI",
  "AI Health Assistant"
]


Skill filtering is handled at the application layer for reliability with SQLite JSON fields.

🖥️ Frontend

A lightweight frontend is provided using plain HTML and JavaScript.

Features:

Load profile data

Search projects by skill

Consume backend APIs using Fetch API

📄 File: frontend/index.html

🔐 Admin Panel

Django Admin is enabled for managing profiles and projects.

http://127.0.0.1:8000/admin/

⚙️ Setup Instructions
1. Clone Repository
git clone <repo-url>
cd me-api-playground

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Start Server
python manage.py runserver

✅ Acceptance Criteria Checklist

✔ Health endpoint returns 200

✔ REST APIs implemented

✔ Database schema defined

✔ Real data seeded

✔ Skill-based query supported

✔ Frontend consuming APIs

✔ Admin panel enabled

🧠 Design Decisions

Used Django REST Framework for clean API architecture

Chose SQLite for simplicity and portability

Implemented skill filtering in application logic to avoid SQLite JSON limitations

Minimal frontend to demonstrate API usage

📌 Author

Arun Gupta

GitHub: https://github.com/Arun912003

LinkedIn: https://linkedin.com/in/arun

## 🖥️ Frontend
A minimal HTML/JavaScript frontend is included in the repository for local testing and demonstration of the backend APIs.

Note:
- The frontend is intentionally lightweight and framework-free.
- Live frontend deployment is optional for this backend-focused assessment.
- Core evaluation is based on API functionality and responses.

---

## 🔐 Admin Panel
The application includes Django Admin for internal data management (profiles and projects).

Note:
- Admin access is intended for development and maintenance purposes only.
- Admin credentials are environment-specific and are not shared publicly.
- Assessment evaluation focuses on REST API functionality, not admin authentication.


🏁 Final Notes

This project is designed to be simple, readable, and assessment-focused, demonstrating backend fundamentals, API design, and real-world debugging.