from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=100)
    std = models.IntegerField()
    rollno = models.IntegerField()
    email = models.EmailField(max_length=100)
    grade = models.CharField(max_length=20)


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    doj = models.DateField(null=False)
    exp = models.IntegerField()
    salary = models.FloatField(null=False)


class Course(models.Model):
    subject = models.CharField(max_length=100)
    duration = models.TimeField()


