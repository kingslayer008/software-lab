from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    clgname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username


class CourseType(models.Model):
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.course_type


class CourseDes(models.Model):
    course_name = models.CharField(max_length=100, null=True)
    course_id = models.IntegerField(null=True)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course_des = models.CharField(max_length=200, null=True)
    course_year = models.DateField(null=True)
    course_price = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.course_name


class RegCourses(models.Model):
    user_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
