from django.db import models


class Registration(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField(default="01.01.2000")
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


