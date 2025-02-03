from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required
@user_passes_test(lambda u: u.is_admin)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
        'is_admin': request.user.is_authenticated and request.user.is_admin,  # Check if the user is admin
    }
    return render(request, 'courses/course_list.html', context)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list'
                            '')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})
