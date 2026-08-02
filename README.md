# 💬 Chatterbox - Real-Time Django Chat Application

[![Django](https://img.shields.io/badge/Django-4.x-092E20.svg?style=flat&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A full-stack web chat application built with **Django** enabling users to create discussion channels, exchange messages in real-time, and manage user accounts with a clean, responsive UI.

---

## 🚀 Key Features

- **User Authentication:** Secure signup, login, logout, and session management.
- **Chat Channels / Rooms:** Dynamic room creation and topic-focused message boards.
- **Responsive Interface:** Mobile-friendly frontend UI for seamless desktop and mobile messaging.
- **ORM Persistence:** Relational data architecture mapping user profiles, channels, and message history.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django Web Framework
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** Django Templates, HTML5, CSS3

---

## ⚙️ Local Setup & Installation

```bash
# Clone repository
git clone https://github.com/ManaliS24/Chat_App_django.git
cd Chat_App_django

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install django

# Run database migrations
python chatterbox/manage.py migrate

# Start local development server
python chatterbox/manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.
