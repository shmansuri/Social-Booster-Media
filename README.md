# Django REST API Demo – Full Stack Assignment

## Project Overview

This project is a simple backend web application built using **Python (Django)** and **Django REST Framework**, developed as part of a demo task for the Full Stack Developer role.

The application demonstrates:

* RESTful CRUD operations
* PostgreSQL database integration
* Third-party API integration
* Basic reporting/analytics using database data

The focus of this project is on **clean backend architecture, API design, and real-world integration**, rather than UI complexity.

---

## Tech Stack

* **Backend Framework:** Django 5.x
* **API Framework:** Django REST Framework (DRF)
* **Database:** PostgreSQL (Supabase – Direct Connection)
* **Third-Party API:** JSONPlaceholder
* **Deployment:** Cloud-hosted (publicly accessible URL)
* **Tools:** Python, REST APIs, GitHub

---

## Features

### 1. CRUD Operations (REST APIs)

The application provides complete CRUD functionality for managing student records using DRF ViewSets.

**Student Fields:**

* Roll Number (unique)
* Name
* Age
* Address
* Course

**Endpoints:**

* `GET /api/students/` – List all students
* `POST /api/students/` – Create a new student
* `GET /api/students/{id}/` – Retrieve student details
* `PUT /api/students/{id}/` – Update student details
* `DELETE /api/students/{id}/` – Delete a student

---

### 2. Third-Party API Integration

A third-party REST API is integrated to demonstrate external API consumption.

* **API Used:** JSONPlaceholder
* **Purpose:** Fetch external user data and return it through a custom endpoint

**Endpoint:**

* `GET /api/external/jsonplaceholder-users/`

This endpoint fetches data from an external service, handles errors gracefully, and returns the response in JSON format.

---

### 3. Reporting / Analytics Feature

A simple reporting endpoint is implemented using database aggregation to provide insights from stored data.

**Example Report:**

* Number of students grouped by course

**Endpoint:**

* `GET /api/report/students/`

This demonstrates backend data analysis and reporting without relying on frontend visualization libraries.

---

## Database Configuration

* PostgreSQL is used as the primary database.
* Supabase PostgreSQL is connected using **Direct Connection**, which is compatible with Django ORM.
* Environment variables are used to manage sensitive credentials securely.

---

## Setup Instructions (Local)

1. **Clone the repository**

```bash
git clone <repository-url>
cd <project-folder>
```

2. **Create virtual environment & activate**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
   Create a `.env` file using `.env.example` and add database credentials.

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Start the server**

```bash
python manage.py runserver
```

---

## Live Deployment

The application is deployed and publicly accessible.

**Live URL:**

```
<live-deployment-link>
```

All APIs can be tested directly using the above URL.

---

## Notes

* The project focuses on backend development and API design.
* Authentication is intentionally kept open for easy testing.
* Code structure follows Django REST Framework best practices.

---

## Author

**Saddam Hussain Mansuri**

Full Stack Developer | Python | Django | Django REST Framework
