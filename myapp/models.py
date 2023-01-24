from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='media')


class UserInfo(models.Model):
    u_id = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.u_id


class StudentInfo(models.Model):
    sid = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
    image = models.FileField(storage=fs, upload_to="student_pic")

    def __str__(self):
        return self.sid


class EmployeeInfo(models.Model):
    eid = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.eid



