from django.db import models
from users.models import User
from courses.models import Course


class Registration(models.Model):
    """This is a registration class"""
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} registered for {self.course.name}'
