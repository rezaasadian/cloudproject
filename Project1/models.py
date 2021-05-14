from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone = models.IntegerField()
    specialty = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

class VisitTime(models.Model):
    date = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)

class UserVisit(models.Model):
    STATUS = (
        ("reserved", "رزرو شده"),
        ("open", "خالی"),
        ("canceled", "لغو شده")
    )
    status = models.CharField(max_length=10, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    visittime = models.ForeignKey(VisitTime, on_delete=models.DO_NOTHING)


class Comment(models.Model):
    commenttext = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)