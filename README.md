🔐 FastAPI Auth-Based Task API

A secure, production-structured multi-user Task Management REST API built with FastAPI, SQLAlchemy ORM, and JWT authentication.

This project demonstrates secure backend architecture, ownership enforcement, and scalable API design.

🚀 Features :

🔑 Authentication - 
1. User registration
2. Secure password hashing using bcrypt
3. JWT access token generation
4. OAuth2 password flow
5. Protected routes using dependency injection

📋 Task Management (User-Specific) -
1. Create task
2. Get all tasks (with filtering & pagination)
3. Get single task
4. Update task (partial updates supported)
5. Delete task
6. Ownership enforcement (users can access only their own tasks)

⚙ Production-Level Enhancements -
1. SQLAlchemy ORM relationships
2. Cascade delete support
3. Environment variable configuration (.env)
4. Pagination (limit, offset)
5. Filtering (completed=true/false)
6. Proper HTTP status codes
7. 204 No Content for delete operations


🏗 Tech Stack :

1. Python
2. FastAPI
3. SQLAlchemy ORM
4. SQLite
5. JWT (python-jose)
6. Passlib (bcrypt)
7. OAuth2 Password Flow
8. python-dotenv


🔑 Authentication Flow :

1. Register a new user
2. Login with email & password
3. Receive JWT access token
4. Authorize via Swagger UI
5. Access protected /task endpoints


📌 API Endpoints :
🔑 Authentication -
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | login & receive JWT |

🔑 Authentication -
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks | Create new user |
| GET | /tasks | Get all tasks (filter & paginate) |
| GET | /tasks/{task_id} | Get single task |
| PATCH | /tasks/{task_id} | Update task |
| DELETE | /tasks/{task_id} | Delete task |


🔐 Security Design :
1. JWT stored in Authorization header
2. Token required for all task routes
3. Ownership enforcement at database query level
4. 404 returned for unauthorized task access (prevents data leakage)
5. Passwords hashed using bcrypt
6. Secrets managed via .env file


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

🎯 Key Learning Outcomes :
1. Implement JWT authentication in FastAPI
2. Secure API routes using dependency injection
3. Design multi-user systems with ownership enforcement
4. Implement pagination & filtering
5. Structure scalable backend projects
6. Use environment-based configuration
7. Apply REST best practices