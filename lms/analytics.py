from datetime import datetime

from .mongodb import learning_analytics

def save_progress(student_id, lesson_id):

    learning_analytics.insert_one({
        "student_id": student_id,
        "lesson_id": lesson_id,
        "timestamp": datetime.utcnow()
    })