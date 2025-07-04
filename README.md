# 🧠 TaskTracker – Django REST API Mini Project

A simple yet powerful task management system built using Django.  
Designed for learning and showcasing full-stack backend skills including REST API, middleware, logging, Docker, and deployment.

---

## 🚀 Features

- 🔐 User authentication (login/logout)
- 👨‍💼 Admin panel to manage users and tasks
- ✅ Create, update, delete, and assign tasks
- 📡 REST API using Django REST Framework
- 🧾 Built-in logging and error handling
- ⚙️ Custom middleware to track requests
- 🐳 Dockerized for production (coming in Day 3)
- ☁️ Deployable to Render or Heroku (Day 3)

---

## 📂 Folder Structure

```
.
├── tracker/              # App for task management
├── tasktracker/          # Django project settings
├── templates/            # HTML templates
├── db.sqlite3            # SQLite database
├── tasktracker.log       # Logs for errors and requests
└── manage.py
```

---

## 🛠️ Built With

- Python 3
- Django
- Django REST Framework
- SQLite3
- Postman (for API testing)
- Docker (to be added)
- Git + GitHub for version control

---

## 🔧 How to Run the Project Locally

1. Clone the Repository:

```bash
git clone https://github.com/BHiwot/django-tasktracker.git
cd django-tasktracker
```

2. Create a Virtual Environment:

```bash
python -m venv venv
# Activate it:
venv\Scripts\activate        # On Windows
source venv/bin/activate       # On Mac/Linux
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Run Migrations & Create Admin User:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Start the Development Server:

```bash
python manage.py runserver
```

---

## 📘 API Documentation

> All endpoints require **Basic Auth**

### Base URL

```
http://127.0.0.1:8000/api/tasks/
```

### Endpoints

| Method | URL                     | Description         |
|--------|-------------------------|---------------------|
| GET    | `/api/tasks/`           | List all tasks      |
| POST   | `/api/tasks/`           | Create a new task   |
| GET    | `/api/tasks/<id>/`      | Retrieve one task   |
| PUT    | `/api/tasks/<id>/`      | Update a task       |
| DELETE | `/api/tasks/<id>/`      | Delete a task       |

### Sample Request (POST)

```json
{
  "title": "Write Report",
  "description": "Prepare Q2 summary",
  "assigned_to": 1,
  "status": "PENDING"
}
```

---

## 🧪 Postman Collection

A ready-made Postman collection is available to test all API endpoints.

---

## 📌 Deployment

- ✅ Token-based auth using JWT
- 🐳 Docker + Docker Compose
- 🌍 Deployment to cloud (Render)

---

## 👤 Author

Hiwot Berhanu  
📬 GitHub: [@BHiwot](https://github.com/BHiwot)

---

## 📃 License

This project is licensed under the MIT License.
