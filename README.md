# Simple LMS (Django + Docker)

## 📌 Deskripsi

Project ini adalah setup environment development untuk aplikasi **Simple LMS** menggunakan:

* Django
* Docker
* PostgreSQL

Project ini dibuat untuk memahami containerization dan integrasi backend modern.

---

## 🛠️ Teknologi

* Python 3.11
* Django
* PostgreSQL
* Docker & Docker Compose

---

## 📁 Struktur Project

```
simple-lms/ 
├── config/ 
│ ├── __init__.py 
│ ├── asgi.py 
│ ├── settings.py 
│ ├── urls.py 
│ └── wsgi.py 
├── .env 
├── .env.example 
├── .gitignore 
├── docker-compose.yml 
├── Dockerfile 
├── manage.py 
├── requirements.txt 
└── README.md
```

---

## ⚙️ Cara Menjalankan Project

### 1. Clone Repository

```
git clone https://github.com/Syafunn/simple-lms.git
cd simple-lms
```

### 2. Copy Environment File

```
cp .env.example .env
```

### 3. Build & Run Docker

```
docker compose up --build
```

### 4. Jalankan Migration

```
docker compose exec web python manage.py migrate
```

### 5. Akses Aplikasi

Buka browser:

```
http://localhost:8000
```

---

## 🔐 Environment Variables

| Variable    | Deskripsi          |
| ----------- | ------------------ |
| DEBUG       | Mode debug Django  |
| DB_NAME     | Nama database      |
| DB_USER     | User PostgreSQL    |
| DB_PASSWORD | Password database  |
| DB_HOST     | Host database (db) |
| DB_PORT     | Port database      |

---

## 🐳 Services (Docker Compose)

### 1. Web (Django)

* Port: 8000
* Menjalankan aplikasi Django

### 2. Database (PostgreSQL)

* Port: 5432
* Menyimpan data aplikasi

---

## 📸 Screenshot

### Django Welcome Page

<img width="2560" height="1504" alt="Screenshot 2026-03-26 203502" src="https://github.com/user-attachments/assets/e35672c6-e59f-42fe-86f6-fc0f50f0191b" />

---

## ✅ Fitur yang Berjalan

* Docker Compose berhasil running
* Django dapat diakses di localhost:8000
* PostgreSQL terkoneksi
* Environment variables digunakan
* Struktur project sesuai best practice

