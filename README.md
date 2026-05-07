<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=30&pause=1000&color=2E75B6&center=true&vCenter=true&width=700&lines=Exhibition+Participation+Management;System+%F0%9F%8F%86;Track+%C2%B7+Manage+%C2%B7+Analyze" alt="Typing SVG" />

<br/>

<img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge&logo=git" />
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-16+-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

<br/><br/>

> **EPMS** — A robust Management Information System for tracking, managing, and analyzing student participation across science and technology exhibitions.

<br/>

[📖 Documentation](#-documentation) · [🚀 Quick Start](#-quick-start) · [📡 API Reference](#-api-reference) · [🤝 Contributing](#-contributing) · [🐛 Report Bug](https://github.com/khamisngofi-web/epms/issues)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [API Reference](#-api-reference)
- [Database Schema](#-database-schema)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About the Project

The **Exhibition Participation Management System (EPMS)** is a backend-first MIS designed to streamline the entire lifecycle of science and technology exhibition events — from student registration and project submission, all the way to results tracking and historical reporting.

Built with a clean layered architecture, EPMS provides institutions, coordinators, and students with a centralised platform to:

- 📋 **Register** students and their exhibition projects
- 🏛️ **Manage** exhibition events, categories, and schedules
- 📊 **Track** participation history and performance over time
- 🏆 **Record** results, awards, and judge evaluations
- 📈 **Generate** analytical reports for institutional decision-making

> This project is developed as part of a real-world MIS learning initiative, applying industry-standard backend practices.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎓 **Student Management** | Register and manage student profiles, departments, and academic years |
| 🏛️ **Exhibition Management** | Create and manage exhibitions with categories, dates, and venues |
| 📋 **Project Submission** | Submit, update, and track project entries per exhibition |
| 👨‍⚖️ **Judge Management** | Assign judges to categories and record evaluations |
| 🏆 **Results & Awards** | Record scores, rank participants, and issue award certificates |
| 📊 **Analytics Dashboard** | Aggregated reports on participation trends and performance |
| 🔐 **Role-Based Access** | Admin, Coordinator, Judge, and Student access levels via JWT |
| 📡 **REST API** | Fully documented OpenAPI/Swagger interface |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                         │
│              (Web Browser / Mobile / API Client)            │
└───────────────────────────┬─────────────────────────────────┘
                            │  HTTP / REST
┌───────────────────────────▼─────────────────────────────────┐
│                       API LAYER (FastAPI)                   │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐   │
│   │ /students│  │/exhibiti-│  │/projects │  │ /results  │   │
│   │  router  │  │ons router│  │  router  │  │  router   │   │ 
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └─────┬─────┘   │
└────────┼─────────────┼─────────────┼───────────────┼────────┘
         │             │             │               │
┌────────▼─────────────▼─────────────▼───────────────▼────────┐
│                     SERVICE LAYER                           │
│         Business Logic · Validation · Orchestration         │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│                   REPOSITORY LAYER                          │
│              SQLAlchemy 2.0 Async ORM Queries               │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│                   DATABASE LAYER                            │
│              PostgreSQL · Alembic Migrations                │
└─────────────────────────────────────────────────────────────┘
```

**Design Pattern:** Routes → Services → Repositories → Models  
**Auth:** JWT Bearer tokens with role-based permissions  
**Validation:** Pydantic v2 schemas on all inputs/outputs

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.11+ | Core runtime |
| **Framework** | FastAPI 0.110+ | REST API & OpenAPI docs |
| **ORM** | SQLAlchemy 2.0 (async) | Database abstraction |
| **Database** | PostgreSQL 16+ | Primary data store |
| **Migrations** | Alembic | Schema version control |
| **Validation** | Pydantic v2 | Request/response schemas |
| **Auth** | JWT (python-jose) | Authentication & authorisation |
| **Testing** | pytest + httpx | Unit & integration tests |
| **Dev Server** | Uvicorn | ASGI server |
| **Env Config** | python-dotenv | Environment management |

---

## 📁 Project Structure

```
epms/
├── 📁 app/
│   ├── 📁 api/
│   │   ├── 📁 v1/
│   │   │   ├── students.py       # Student endpoints
│   │   │   ├── exhibitions.py    # Exhibition endpoints
│   │   │   ├── projects.py       # Project submission endpoints
│   │   │   ├── results.py        # Results & awards endpoints
│   │   │   └── auth.py           # Authentication endpoints
│   │   └── deps.py               # Shared dependencies (auth, db)
│   │
│   ├── 📁 core/
│   │   ├── config.py             # App configuration (env vars)
│   │   ├── security.py           # JWT creation & verification
│   │   └── database.py           # Async DB engine & session
│   │
│   ├── 📁 models/
│   │   ├── student.py            # Student ORM model
│   │   ├── exhibition.py         # Exhibition ORM model
│   │   ├── project.py            # Project ORM model
│   │   └── result.py             # Result & award ORM model
│   │
│   ├── 📁 schemas/
│   │   ├── student.py            # Pydantic schemas for students
│   │   ├── exhibition.py         # Pydantic schemas for exhibitions
│   │   ├── project.py            # Pydantic schemas for projects
│   │   └── result.py             # Pydantic schemas for results
│   │
│   ├── 📁 services/
│   │   ├── student_service.py    # Student business logic
│   │   ├── exhibition_service.py # Exhibition business logic
│   │   └── result_service.py     # Scoring & ranking logic
│   │
│   ├── 📁 repositories/
│   │   ├── student_repo.py       # Student DB queries
│   │   ├── exhibition_repo.py    # Exhibition DB queries
│   │   └── result_repo.py        # Result DB queries
│   │
│   └── main.py                   # App entry point & router mount
│
├── 📁 alembic/                   # Database migrations
│   ├── versions/
│   └── env.py
│
├── 📁 tests/
│   ├── test_students.py
│   ├── test_exhibitions.py
│   └── test_results.py
│
├── .env.example                  # Environment variable template
├── requirements.txt              # Python dependencies
├── alembic.ini                   # Alembic config
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

Make sure you have the following installed:

- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL 16+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/khamisngofi-web/epms.git
cd epms
```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux / macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/epms_db

# Security
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
APP_NAME=EPMS
DEBUG=True
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start the Server

```bash
uvicorn app.main:app --reload
```

### 7. Open API Docs

Visit **[http://localhost:8000/docs](http://localhost:8000/docs)** for the interactive Swagger UI.

```
🌐 Swagger UI  →  http://localhost:8000/docs
📘 ReDoc       →  http://localhost:8000/redoc
💓 Health      →  http://localhost:8000/health
```

---

## 📡 API Reference

### Authentication

```http
POST /api/v1/auth/login
POST /api/v1/auth/register
POST /api/v1/auth/refresh
```

### Students

```http
GET    /api/v1/students              # List all students
POST   /api/v1/students              # Register a new student
GET    /api/v1/students/{id}         # Get student details
PUT    /api/v1/students/{id}         # Update student
DELETE /api/v1/students/{id}         # Remove student
GET    /api/v1/students/{id}/history # Student participation history
```

### Exhibitions

```http
GET    /api/v1/exhibitions           # List all exhibitions
POST   /api/v1/exhibitions           # Create a new exhibition
GET    /api/v1/exhibitions/{id}      # Get exhibition details
PUT    /api/v1/exhibitions/{id}      # Update exhibition
GET    /api/v1/exhibitions/{id}/participants  # List participants
```

### Projects

```http
POST   /api/v1/projects              # Submit a project
GET    /api/v1/projects/{id}         # Get project details
PUT    /api/v1/projects/{id}         # Update submission
GET    /api/v1/projects?exhibition={id}  # Filter by exhibition
```

### Results & Analytics

```http
POST   /api/v1/results               # Record a result
GET    /api/v1/results/{exhibition_id}/rankings  # Get ranked results
GET    /api/v1/analytics/summary     # Participation overview report
GET    /api/v1/analytics/trends      # Year-on-year trends
```

> 📘 Full interactive documentation available at `/docs` when the server is running.

---

## 🗄️ Database Schema

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│   students   │     │   exhibitions   │     │     projects     │
├──────────────┤     ├─────────────────┤     ├──────────────────┤
│ id (PK)      │     │ id (PK)         │     │ id (PK)          │
│ full_name    │     │ name            │     │ title            │
│ reg_number   │◄────┤ category        │────►│ description      │
│ department   │     │ venue           │     │ student_id (FK)  │
│ year_of_study│     │ date            │     │ exhibition_id(FK)│
│ email        │     │ status          │     │ category         │
│ created_at   │     │ created_at      │     │ submitted_at     │
└──────────────┘     └─────────────────┘     └────────┬─────────┘
                                                       │
                     ┌─────────────────┐               │
                     │    results      │               │
                     ├─────────────────┤               │
                     │ id (PK)         │               │
                     │ project_id (FK) │◄──────────────┘
                     │ judge_id (FK)   │
                     │ score           │
                     │ rank            │
                     │ award           │
                     │ notes           │
                     │ evaluated_at    │
                     └─────────────────┘
```

---

## 🗺️ Roadmap

- [x] Project scaffolding & architecture setup
- [x] Database models (SQLAlchemy 2.0 async)
- [x] Pydantic v2 schemas
- [x] Student management endpoints
- [ ] Exhibition management endpoints
- [ ] Project submission & tracking
- [ ] JWT Authentication & role-based access
- [ ] Judge management module
- [ ] Results & scoring system
- [ ] Analytics & reporting endpoints
- [ ] Unit & integration test suite
- [ ] Dockerize the application
- [ ] Frontend dashboard (React)
- [ ] Deployment (CI/CD pipeline)

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "feat: add amazing feature"

# 4. Push to your branch
git push origin feature/amazing-feature

# 5. Open a Pull Request
```

Please follow the [Conventional Commits](https://www.conventionalcommits.org/) format for commit messages.

---

## 👨‍💻 Author

<div align="center">

**Khamis Mgofi**

Backend Developer · CS Student · Python Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-khamisngofi--web-181717?style=flat&logo=github)](https://github.com/khamisngofi-web)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/khamisngofi)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **Khamis Ngofi**

⭐ Star this repo if you found it helpful!

</div>
