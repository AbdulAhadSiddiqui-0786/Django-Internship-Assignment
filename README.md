# 🛠️ Django Internship Assignment

This project showcases backend development using Django REST Framework, Token Authentication, Celery background tasks, and Telegram Bot integration. It follows production-grade practices including environment variable handling and clean code organization.

---

## 🚀 Features Implemented

- ✅ Django REST Framework APIs
- 🔐 Token Authentication (JWT or DRF TokenAuth)
- 🌐 Public & Protected API endpoints
- ⚙️ Celery + Redis integration
- 🤖 Telegram Bot integration (`/start` command)
- 🔒 Environment variables for secret management
- 🧪 Testable and scalable backend structure

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
###2. Create & Activate Virtual Environment
python -m venv env
env\Scripts\activate      # Windows
# OR
source env/bin/activate   # macOS/Linux

3. Install Dependencies3. Install Dependencies

   pip install -r requirements.txt
4. Create .env File
  Create a .env file in the root directory:
  SECRET_KEY=your_django_secret_key
  DEBUG=False
  ALLOWED_HOSTS=127.0.0.1,localhost
  TELEGRAM_TOKEN=your_telegram_bot_token
  EMAIL_HOST=smtp.example.com
  EMAIL_PORT=587
  EMAIL_HOST_USER=your_email@example.com
  EMAIL_HOST_PASSWORD=your_email_password


| Method | Endpoint          | Auth Required | Description               |
| ------ | ----------------- | ------------- | ------------------------- |
| GET    | `/api/public/`    | ❌ No          | Public access             |
| GET    | `/api/protected/` | ✅ Yes         | JWT or DRF Token required |

Authorization: Token your_token_here
Celery with Redis
Start Redis Server
Make sure Redis is installed and running:
redis-server
Start Celery Worker
celery -A internship_project worker --loglevel=info

Telegram Bot Integration
Create bot via @BotFather.

Add token in .env file.

Bot listens to /start command and stores Telegram username to database.

To run bot (if separate):
python telegram_bot.py

internship_project/
├── core/
│   ├── views.py          # API views
│   ├── models.py         # User & Telegram models
│   ├── urls.py           # App routing
├── internship_project/
│   ├── settings.py       # Environment-aware config
│   ├── celery.py         # Celery config
├── manage.py
├── requirements.txt
├── .env                  # Environment variables
├── README.md
└── .gitignore


| Variable         | Description                           |
| ---------------- | ------------------------------------- |
| `SECRET_KEY`     | Django secret key                     |
| `DEBUG`          | Should be set to `False`              |
| `ALLOWED_HOSTS`  | Comma-separated list of allowed hosts |
| `TELEGRAM_TOKEN` | Telegram Bot token                    |
| `EMAIL_*`        | Email backend config for Celery task  |

✅ Submission Checklist
 Django project with DRF and TokenAuth

 Celery task and Redis configured

 Telegram bot integrated

 Clean commit history

 This README.md completed

 Uploaded to GitHub

  Author
Abdul Ahad Siddiqui
Backend Developer — Internship Candidate
Feel free to reach out via Telegram or email.

