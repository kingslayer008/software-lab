from django.contrib import admin
from e_app.models import UserProfileInfo, CourseType, CourseDes, RegCourses
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(CourseDes)
admin.site.register(CourseType)
admin.site.register(RegCourses)
