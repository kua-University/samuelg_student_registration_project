from django.urls import path
from . import views

urlpatterns = [
    path(
        "register/<int:course_id>/", views.register_for_course, name="course_register"
    ),
]
