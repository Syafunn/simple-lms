from ninja import NinjaAPI
from pydantic import BaseModel
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from jose import jwt
from datetime import datetime, timedelta
from ninja.security import HttpBearer

from .models import Course, Category, Enrollment, Progress

api = NinjaAPI()
User = get_user_model()

# =========================
# JWT CONFIG
# =========================
SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except:
            return None


# =========================
# SCHEMA
# =========================
class RegisterSchema(BaseModel):
    username: str
    password: str
    role: str


class LoginSchema(BaseModel):
    username: str
    password: str


class CourseSchema(BaseModel):
    title: str
    description: str
    category_id: int


# =========================
# ROLE CHECK
# =========================
def is_instructor(user):
    return user.get("role") == "instructor"


def is_admin(user):
    return user.get("role") == "admin"


def is_student(user):
    return user.get("role") == "student"


# =========================
# AUTH
# =========================
@api.post("/auth/register")
def register(request, data: RegisterSchema):
    user = User.objects.create_user(
        username=data.username,
        password=data.password,
        role=data.role
    )
    return {"message": "User created"}


@api.post("/auth/login")
def login(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)

    if not user:
        return {"error": "Invalid username or password"}

    token = create_access_token({
        "user_id": user.id,
        "username": user.username,
        "role": user.role
    })

    return {"access_token": token}


@api.get("/auth/me", auth=AuthBearer())
def me(request):
    return request.auth


@api.put("/auth/me", auth=AuthBearer())
def update_me(request, data: dict):
    user_data = request.auth
    user = User.objects.get(id=user_data["user_id"])

    user.username = data.get("username", user.username)
    user.save()

    return {"message": "Updated"}


# =========================
# COURSES (PUBLIC)
# =========================
@api.get("/courses")
def list_courses(request):
    courses = Course.objects.all()
    return [
        {
            "id": c.id,
            "title": c.title,
            "instructor": c.instructor.username
        }
        for c in courses
    ]


@api.get("/courses/{course_id}")
def course_detail(request, course_id: int):
    c = Course.objects.get(id=course_id)
    return {
        "id": c.id,
        "title": c.title,
        "description": c.description,
        "instructor": c.instructor.username
    }


# =========================
# COURSES (PROTECTED)
# =========================
@api.post("/courses", auth=AuthBearer())
def create_course(request, data: CourseSchema):
    user = request.auth

    if not is_instructor(user):
        return {"error": "Only instructor can create course"}

    instructor = User.objects.get(id=user["user_id"])
    category = Category.objects.get(id=data.category_id)

    course = Course.objects.create(
        title=data.title,
        description=data.description,
        instructor=instructor,
        category=category
    )

    return {"message": "Course created", "id": course.id}


@api.patch("/courses/{id}", auth=AuthBearer())
def update_course(request, id: int, data: CourseSchema):
    user = request.auth
    course = Course.objects.get(id=id)

    if user["user_id"] != course.instructor.id:
        return {"error": "Not owner"}

    course.title = data.title
    course.description = data.description
    course.save()

    return {"message": "Updated"}


@api.delete("/courses/{id}", auth=AuthBearer())
def delete_course(request, id: int):
    user = request.auth

    if not is_admin(user):
        return {"error": "Admin only"}

    Course.objects.filter(id=id).delete()
    return {"message": "Deleted"}


# =========================
# ENROLLMENT
# =========================
@api.post("/enrollments", auth=AuthBearer())
def enroll(request, course_id: int):
    user = request.auth

    if not is_student(user):
        return {"error": "Student only"}

    Enrollment.objects.create(
        student_id=user["user_id"],
        course_id=course_id
    )

    return {"message": "Enrolled"}


@api.get("/enrollments/my-courses", auth=AuthBearer())
def my_courses(request):
    user = request.auth

    enrollments = Enrollment.objects.filter(student_id=user["user_id"])

    return [
        {
            "course_id": e.course.id,
            "course": e.course.title
        }
        for e in enrollments
    ]


# =========================
# PROGRESS
# =========================
@api.post("/enrollments/{id}/progress", auth=AuthBearer())
def mark_progress(request, id: int, lesson_id: int):
    user = request.auth

    Progress.objects.update_or_create(
        student_id=user["user_id"],
        lesson_id=lesson_id,
        defaults={"completed": True}
    )

    return {"message": "Progress updated"}


@api.get("/progress", auth=AuthBearer())
def get_progress(request):
    user = request.auth

    progress = Progress.objects.filter(student_id=user["user_id"])

    return [
        {
            "lesson_id": p.lesson.id,
            "lesson_title": p.lesson.title,
            "completed": p.completed
        }
        for p in progress
    ]