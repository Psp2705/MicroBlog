# 🧪 Flask Mega-Tutorial Practice Project

It is a complete, hands-on learning journey to build a real-world microblog web application using Flask.

---

## 🚀 Project Overview

- Develop a microblogging platform using Flask
- Learn about routing, templates, web forms, databases, authentication, and more
- Implement SQLAlchemy for ORM and Alembic for database migrations
- Integrate user login and registration system
- Extend with features like followers, posts, full-text search, pagination, and REST API

---

## 🛠️ Tech Stack

- **Flask** – Web framework  
- **Flask-WTF** – Web forms with CSRF protection  
- **Flask-Login** – User session management  
- **Flask-Migrate** – Database migrations  
- **SQLAlchemy** – ORM for database models  
- **Bootstrap 4** – UI framework  

---

## 📁 Project Structure

```
MicroBlog/
├── app/
│ ├── templates/
│ ├── static/
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ └── init.py
├── migrations/
├── venv/
├── microblog.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Setup Instructions

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\\Scripts\\activate  # or source venv/bin/activate on macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variables (on PowerShell)
$env:FLASK_APP = "microblog.py"
$env:FLASK_ENV = "development"

# 4. Initialize the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 5. Run the app
flask run
```
---
## 🧠 Learning Goal
- This project is for educational purposes to learn Flask best practices through real-world use cases and evolve a microblog into a full-featured web app.

