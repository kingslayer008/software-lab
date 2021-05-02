from django.shortcuts import render
from e_app.forms import UserForm, UserProfileInfoForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'e_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            return HttpResponse("INVALID LOGIN DETAILS SUPPPLIED")

    return render(request, 'e_app/login.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'e_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def courses(request):
    user = request.user

    courses = CourseDes.objects.all()

    if 'Full stack django web development' in request.POST:
        reg = RegCourses.objects.create(
            user_name=user, course_id='Full stack django web development')

    if 'Introduction to Machine learning' in request.POST:
        reg = RegCourses.objects.create(
            user_name=user, course_id='Introduction to Machine learning')

    if 'Flutter and Dart beginners guide' in request.POST:
        reg = RegCourses.objects.create(
            user_name=user, course_id='Flutter and Dart beginners guide')

    if 'Python bootcamp' in request.POST:
        reg = RegCourses.objects.create(
            user_name=user, course_id='Python bootcamp')

    return render(request, 'e_app/courses.html', {'courses': courses, 'user': user})
