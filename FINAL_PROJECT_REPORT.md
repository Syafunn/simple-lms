# Laporan Final Project - Simple LMS Extended Backend

## 1. Identitas
- Nama: Muhammad Syafan Midhad
- NIM: A11.2023.14923
- Kelas: A11.4618
- Mata Kuliah: Pemrograman Sisi Server
- URL Repository: https://github.com/Syafunn/simple-lms.git

## 2. Deskripsi Project
Project ini dibuat untuk mengembangkan platform Simple Learning Management System (LMS). Di sini saya menggunakan Django Ninja buat bikin REST API yang super cepat, ditambah ekosistem Docker biar semua service bisa jalan bareng dengan rapi. Fokus utama saya di final project ini adalah memperketat sistem keamanan lewat pembagian role user (RBAC), mempercepat akses data pakai Redis, dan bikin proses di belakang layar jadi asinkron pakai Celery dan RabbitMQ supaya aplikasi gak lemot pas ngerjain tugas berat.

## 3. Fitur Dasar (Wajib) yang Telah Berjalan
1. Dockerized Environment: Semua layanan (PostgreSQL, Redis, RabbitMQ, Celery, Flower, dan Django) udah jalan kompak di dalam container Docker Compose.
2. Authentication dan RBAC: Login udah aman pakai JWT token, lengkap dengan pembatasan hak akses buat Admin, Instructor, dan Student.
3. Course API: Fitur buat bikin, liat, edit, dan hapus kelas udah berfungsi dengan ngecek siapa pemilik kelasnya.
4. Enrollment dan Progress: Student bisa daftar kelas dan langsung tracking persentase progres belajar mereka.
5. Interactive API Docs: Dokumentasi endpoint otomatis dan bisa langsung dicoba lewat Swagger UI.

## 4. Fitur Tambahan yang Dipilih (Paket 6 - Async Processing + Caching)
Biar performa aplikasi makin jos, saya milih fitur yang fokus ke optimasi kecepatan dan pemrosesan di latar belakang.

| No | Fitur | Kategori | Poin | Status |
|:---:|---|---|:---:|:---:|
| 1 | Caching menggunakan Redis (List & Detail) | Performa | - | Selesai |
| 2 | Email notification async | Celery & Async | 12 | Selesai |
| 3 | Generate report async | Celery & Async | 18 | Selesai |
| 4 | Scheduled task (Update Course Stats) | Celery & Async | 15 | Selesai |
| 5 | Task status endpoint | Celery & Async | 12 | Selesai |
| 6 | Flower monitoring | Celery & Async | 8 | Selesai |

Penjelasan Cara Kerjanya:
- Redis Cache: Saya pasang di endpoint yang sering dibuka (seperti daftar kelas). Hasilnya, loading jadi instan karena data diambil dari memori Redis, bukan bolak-balik nanya ke database.
- Celery dan RabbitMQ: Pas student klik daftar kelas, aplikasi langsung ngasih respon sukses tanpa nunggu proses kirim email selesai. Tugas kirim email dan bikin laporan CSV yang berat didelegasikan ke Celery worker biar jalan di background.
- Flower dan Task Status: Saya nyediain endpoint buat ngecek apakah laporan CSV udah kelar dibikin atau belum. Kita juga bisa mantau kesehatan antrean tugasnya lewat dashboard visual Flower.

## 5. Akun Demo
- Admin: username: admin | password: admin123 | role: admin
- Instructor: username: instructor | password: instructor123 | role: instructor
- Student: username: student | password: student123 | role: student

## 6. Screenshot / Bukti Pengujian

(Catatan: Semua file gambar ditaruh di folder img/)

A. Bukti Generate Report Async & Task Status (SUCCESS)
![Generate Report Status](img/status_success.png)
Keterangan: Endpoint berhasil ngecek ID tugas dan mengembalikan status SUCCESS beserta lokasi file CSV-nya.

B. Bukti Email Notification Async (Mock / Terminal Log)
![Email Async](img/trigger_report.png)
Keterangan: Tugas pengiriman email langsung kepicu di background begitu student daftar kelas.

C. Bukti Flower Monitoring (Celery Worker Aktif)
![Flower Dashboard](img/flower.png)
Keterangan: Dashboard Flower berhasil mendeteksi worker Celery yang lagi standby dan merekam riwayat tugas.

## 7. Kendala dan Solusi Selama Pengembangan
1. Masalah Hak Akses (RBAC) Laporan: Pas awal dicoba, Admin selalu dapet error gak punya akses buat generate report, padahal token JWT-nya udah bener.
   Solusi: Ternyata masalahnya sepele tapi fatal, yaitu huruf besar-kecil di database (Admin vs admin). Saya langsung perbaiki fungsi pengecekannya pakai method .lower() biar inputnya jadi makin fleksibel dan gak sensitif.
2. Error Registrasi Instructor: Sempat muncul error Unprocessable Entity pas nyoba daftar pakai role Instructor atau Admin, cuma role Student aja yang berhasil.
   Solusi: Saya cek lagi skema Pydantic-nya, ternyata field role kelupaan dimasukkan ke RegisterSchema. Setelah field-nya ditambahin dan fungsi create_user di Django disesuaikan agar gak nge-hardcode role student, fiturnya langsung lancar.

## 8. Kesimpulan
Lewat project ini, saya jadi paham gimana cara bikin backend yang bener-bener siap buat skala produksi. Gak cuma sekadar bikin fitur bisa jalan, tapi juga mikirin gimana caranya biar aplikasi gak gampang tumbang. Penggunaan JWT bikin sistem aman, Redis bikin akses data super cepat, dan Celery sukses bikin tugas berat jadi terasa ringan tanpa mengorbankan kenyamanan pengguna.