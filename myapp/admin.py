from django.contrib import admin
from .models import UserInfo, StudentInfo, EmployeeInfo


admin.site.register(UserInfo)
admin.site.register(StudentInfo)
admin.site.register(EmployeeInfo)

