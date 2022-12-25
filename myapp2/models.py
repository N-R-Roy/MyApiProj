from django.db import models


class PersonInfo(models.Model):
    pid = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.pid


class Singer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=250)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250)
    members = models.ManyToManyField(PersonInfo)

    def __str__(self):
        return self.name
