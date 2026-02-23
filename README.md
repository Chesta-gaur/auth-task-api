🔐 FastAPI Auth-Based Task API

A secure multi-user task management REST API built with FastAPI, SQLAlchemy, and JWT authentication.

🚀 Features :

1. User Registration
2. Secure Password Hashing (bcrypt)
3. JWT Authentication
4. OAuth2 Password Flow
5. Protected Routes
6. User-specific task management
7. SQLite Database
8. Dependency-based DB session handling

🏗 Tech Stack :

1. Python
2. FastAPI
3. SQLAlchemy ORM
4. SQLite
5. JWT (python-jose)
6. Passlib (bcrypt)

🔑 Authentication Flow :

1. Register user
2. Login with email & password
3. Receive JWT access token
4. Authorize via Swagger UI
5. Access protected task endpoints

📌 API Endpoints :

- Authentication

1. POST /register
2. POST /login

- Tasks (Protected)

1. POST /tasks
2. GET /tasks
3. PATCH /tasks/{id}
4. DELETE /tasks/{id}

🛠 Installation :

```bash
git clone <repo-url>

cd fastapi-auth-task-api

python -m venv .venv

.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```
Run server :
```bash
python -m uvicorn app.main:app --reload
```

Open :
```bash
http://127.0.0.1.8000/docs
```

🎯 Learning Objectives :

1. Implement authentication in FastAPI
2. Understand JWT token lifecycle
3. Protect routes using dependency injection
4. Design scalable backend architecture