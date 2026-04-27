from django.http import JsonResponse
from django.db.models import Count, Avg
from .models import Course, Enrollment

def course_list_baseline(request):
    courses = Course.objects.all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'instructor': c.instructor.username,
        })

    return JsonResponse({'data': data})


def course_list_optimized(request):
    courses = Course.objects.select_related('instructor').all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'instructor': c.instructor.username,
        })

    return JsonResponse({'data': data})

def course_members_baseline(request):
    courses = Course.objects.all()
    payload = []

    for c in courses:
        member_count = Enrollment.objects.filter(course=c).count()
        payload.append({
            'course': c.title,
            'member_count': member_count,
        })

    return JsonResponse({'data': payload})


def course_members_optimized(request):
    courses = Course.objects.annotate(
        member_count=Count('enrollment')  
    )

    payload = []

    for c in courses:
        payload.append({
            'course': c.title,
            'member_count': c.member_count,
        })

    return JsonResponse({'data': payload})

def course_dashboard_baseline(request):
    courses = Course.objects.all()

    total_courses = courses.count()

    total_enrollments = 0
    for c in courses:
        total_enrollments += Enrollment.objects.filter(course=c).count()

    avg_enrollment = total_enrollments / total_courses if total_courses > 0 else 0

    return JsonResponse({
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'avg_enrollment': avg_enrollment,
    })


def course_dashboard_optimized(request):
    stats = Course.objects.annotate(
        member_count=Count('enrollment') 
    ).aggregate(
        total_courses=Count('id'),
        total_enrollments=Count('enrollment'),
        avg_enrollment=Avg('member_count'),
    )

    return JsonResponse(stats)

