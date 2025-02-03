from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_service, name='users_service'),
    path('courses/', views.courses_service, name='courses_service'),
    path('registration/', views.registration_service, name='registration_service'),
    path('payments/', views.payments_service, name='payments_service'),
]
