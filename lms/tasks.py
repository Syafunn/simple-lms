from celery import shared_task
from django.core.mail import send_mail

from .models import Enrollment, Course


@shared_task
def send_enrollment_email(student_id, course_id):

    print(
        f"Enrollment email sent to student {student_id} for course {course_id}"
    )

    return "email sent"


@shared_task
def generate_certificate(student_id, course_id):

    print(
        f"Certificate generated for student {student_id}"
    )

    return "certificate generated"


@shared_task
def update_course_statistics():

    courses = Course.objects.all()

    for course in courses:

        total = Enrollment.objects.filter(
            course=course
        ).count()

        print(
            f"{course.title}: {total} enrollments"
        )

    return "statistics updated"


@shared_task
def export_course_report():

    import csv

    filename = "course_report.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Course ID",
            "Title"
        ])

        for course in Course.objects.all():

            writer.writerow([
                course.id,
                course.title
            ])

    return filename