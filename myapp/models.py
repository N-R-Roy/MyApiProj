from django.db import models


class StudentInfo(models.Model):
    sid = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
    image = models.ImageField(upload_to="student_pic")

    def __str__(self):
        return self.sid


class EmployeeInfo(models.Model):
    eid = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.eid


class UserInfo(models.Model):
    u_id = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.u_id


