from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.course_list, name='course_list'),
    path('add/', views.add_course, name='add_course'),
]
