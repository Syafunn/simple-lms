Simple LMS - Django + Docker
 Deskripsi

Project ini merupakan implementasi Simple Learning Management System (LMS) menggunakan Django, PostgreSQL, dan Docker.

Project ini mencakup:

Setup environment menggunakan Docker
Konfigurasi Django dengan PostgreSQL
Implementasi data model LMS
Query optimization menggunakan Django ORM
Django Admin interface
 Cara Menjalankan Project
1. Clone Repository
git clone https://github.com/Syafunn/simple-lms.git
cd simple-lms
2. Setup Environment

Copy file environment:

cp .env.example .env
3. Jalankan Docker
docker compose up --build
4. Jalankan Migration
docker compose exec web python manage.py migrate
5. Buat Superuser
docker compose exec web python manage.py createsuperuser
6. Akses Aplikasi
Django: http://localhost:8000
Admin: http://localhost:8000/admin
 Environment Variables
DEBUG=1
POSTGRES_DB=lms_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
 Docker Services
Web (Django)
Menjalankan aplikasi Django
Port: 8000
Database (PostgreSQL)
Database utama aplikasi
Port: 5432
 Data Models
1. User
Custom user menggunakan AbstractUser
Role:
Admin
Instructor
Student
2. Category
Mendukung hierarchical category (parent-child)
3. Course
Relasi ke Instructor dan Category
4. Lesson
Relasi ke Course
Memiliki urutan (ordering)
5. Enrollment
Relasi Student dan Course
Unique constraint
6. Progress
Tracking penyelesaian lesson
 Query Optimization
 Tanpa Optimization
Course.objects.all()
 Dengan Optimization
Course.objects.for_listing()

Menggunakan:

select_related()
prefetch_related()

Untuk menghindari N+1 Query Problem dan meningkatkan performa.

##  Screenshot

### Django Welcome Page

<img width="2560" height="1504" alt="Screenshot 2026-03-26 203502" src="https://github.com/user-attachments/assets/e35672c6-e59f-42fe-86f6-fc0f50f0191b" />

Query Optimization Demo


Tanpa Optimization
<img width="725" height="175" alt="Screenshot 2026-04-06 235900" src="https://github.com/user-attachments/assets/de20b319-b7d1-404f-b73e-81a6f9a0afac" />


Dengan Optimization
<img width="760" height="169" alt="Screenshot 2026-04-06 235911" src="https://github.com/user-attachments/assets/60cce8c4-ca50-42df-b6b9-7ef058193552" />

---

Contoh Query
courses = Course.objects.for_listing()

for c in courses:
    print(c.title, c.instructor.username)
 Django Admin

Fitur:

List display informatif
Search functionality
Filter data
Inline Lesson pada Course
 Fixtures

File data awal:

lms_fixture.json

Digunakan untuk mengisi database dengan data awal.

 Project Structure
simple-lms/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
├── manage.py
├── config/
├── lms/
├── screenshots/
└── README.md

 Tech Stack
Django
PostgreSQL
Docker
