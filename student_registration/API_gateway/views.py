from django.shortcuts import render


import requests
from django.http import JsonResponse, HttpResponse

# API Gateway: Forward requests to the Users Service
def users_service(request):
    url = 'http://localhost:8000'  # Users service
    response = requests.request(method=request.method, url=url, data=request.body, headers=request.headers)
    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

# API Gateway: Forward requests to the Courses Service
def courses_service(request):
    url = 'http://localhost:8001/courses/'  # Courses service
    response = requests.request(method=request.method, url=url, data=request.body, headers=request.headers)
    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

# API Gateway: Forward requests to the Registration Service
def registration_service(request):
    url = 'http://localhost:8002/registration/'  # Registration service
    response = requests.request(method=request.method, url=url, data=request.body, headers=request.headers)
    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

# API Gateway: Forward requests to the Payments Service
def payments_service(request):
    url = 'http://localhost:8003/payments/'  # Payments service
    response = requests.request(method=request.method, url=url, data=request.body, headers=request.headers)
    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
