from django.db import models
import os
from django.conf import settings

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(null=True)
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, null=True)


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2000)
    category = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname


class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='static/uploads')

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)





