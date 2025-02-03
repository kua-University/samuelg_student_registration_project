from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration
from .forms import RegistrationForm
from courses.models import Course
def register_for_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = request.user
            registration.course = course
            registration.save()
            return redirect('course_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register_course.html', {'form': form, 'course': course})
