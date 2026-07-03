import time
import csv
from celery import shared_task
from django.core.mail import send_mail
from .models import Enrollment, Course

@shared_task
def send_enrollment_email(student_id, course_id):
    # Simulasi delay kirim email 3 detik
    time.sleep(3)
    print(f"Enrollment email sent to student {student_id} for course {course_id}")
    return "email sent"

@shared_task
def generate_certificate(student_id, course_id):
    # Simulasi delay generate sertifikat PDF 2 detik
    time.sleep(2)
    print(f"Certificate generated for student {student_id}")
    return "certificate generated"

@shared_task
def update_course_statistics():
    courses = Course.objects.all()
    for course in courses:
        total = Enrollment.objects.filter(course=course).count()
        print(f"{course.title}: {total} enrollments")
    return "statistics updated"

@shared_task
def export_course_report():
    print("Mulai meng-generate laporan...")
    
    # Simulasi proses query/pembuatan file yang sangat berat/lama (10 detik)
    time.sleep(10) 
    
    # Simpan di folder /tmp/ agar aman dan terisolasi di dalam container Docker
    filename = "/tmp/course_report.csv"
    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Course ID", "Title"])
        for course in Course.objects.all():
            writer.writerow([course.id, course.title])
            
    print("Laporan selesai dibuat!")
    return filename