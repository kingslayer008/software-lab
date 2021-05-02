from django.contrib import admin
from django.urls import path, include
from e_app import views

app_name = 'e_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name='user_login'),
    path('courses/', views.courses, name="courses"),
]
