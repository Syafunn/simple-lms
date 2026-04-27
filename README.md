#  Simple LMS API (Django Ninja + JWT + RBAC)

##  Deskripsi

Project ini merupakan implementasi **Simple Learning Management System (LMS)** berbasis **REST API** menggunakan:

* Django + Django Ninja
* PostgreSQL
* Docker
* JWT Authentication
* Role-Based Access Control (RBAC)

API ini memungkinkan:

* Manajemen user (Admin, Instructor, Student)
* Manajemen course
* Enrollment student ke course
* Tracking progress pembelajaran

---

##  Fitur Utama

###  Authentication (JWT)

* Register user
* Login (generate token)
* Get & update profile

###  Courses

* List courses (public)
* Detail course
* Create course (Instructor only)
* Update course (Owner only)
* Delete course (Admin only)

###  Enrollment

* Enroll ke course (Student only)
* Melihat course yang diikuti

###  Progress

* Tandai lesson selesai
* Melihat progress belajar

---

##  Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/Syafunn/simple-lms.git
cd simple-lms
```

### 2. Jalankan Docker

```bash
docker-compose up -d --build
```

### 3. Jalankan Migration

```bash
docker-compose exec web python manage.py migrate
```

### 4. Akses API

```text
http://localhost:8000/api/docs
```

---

##  API Documentation (Swagger)

Swagger tersedia di:

```text
/api/docs
```

Gunakan untuk testing semua endpoint.

---

##  Authentication

Gunakan JWT token:

```text
Authorization: Bearer <access_token>
```

---

##  API Endpoints

###  Auth

* POST /api/auth/register
* POST /api/auth/login
* GET /api/auth/me
* PUT /api/auth/me

---

###  Courses

* GET /api/courses
* GET /api/courses/{id}
* POST /api/courses (Instructor)
* PATCH /api/courses/{id} (Owner)
* DELETE /api/courses/{id} (Admin)

---

###  Enrollment

* POST /api/enrollments (Student)
* GET /api/enrollments/my-courses

---

###  Progress

* POST /api/enrollments/{id}/progress
* GET /api/progress

---

##  Role-Based Access Control (RBAC)

| Role       | Akses                  |
| ---------- | ---------------------- |
| Admin      | Delete course          |
| Instructor | Create & update course |
| Student    | Enroll & progress      |

---

##  Database

Menggunakan PostgreSQL dengan Docker container.

---

##  Tech Stack

* Django
* Django Ninja
* PostgreSQL
* Docker
* JWT (python-jose)
* Pydantic

---

##  Screenshots

Berisi:

* Swagger API
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/06c16186-f060-4f30-9fb0-ebf58f16e80a" />

* Login & Token
  <img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/2722265e-186f-4385-a068-4bfe72e65b3c" />

* Create Course, RBAC (success & failed)
  <img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/5fbfeefc-7f29-4856-99e5-15e7eb4b634d" />
  <img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/81b36d65-6259-4b3f-91e3-757682680625" />

* Enrollment
 <img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/59cff465-a777-45bf-a534-d79349163dd1" />

* Progress
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/52d3f9dc-283f-489f-995e-74ca2c2ae834" />


---

##  Project Structure

```
simple-lms/
├── docker-compose.yml
├── requirements.txt
├── config/
├── lms/
└── README.md
```

---

## ✅ Kesimpulan

API LMS berhasil dibangun dengan:

* JWT Authentication
* Role-Based Access Control
* Endpoint lengkap sesuai requirement
* Dokumentasi Swagger

Project siap digunakan dan dikembangkan lebih lanjut.
