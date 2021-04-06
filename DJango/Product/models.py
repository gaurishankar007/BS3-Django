from django.db import models
import os
from django.conf import settings
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(null=True)
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=100, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=100, null=True, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(unique=True, null=True, validators=[validators.validate_email])
    phone = models.CharField(max_length=20, null=True, validators=[validators.MinLengthValidator(7)])


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


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(null=True, max_length=200)
    lastname = models.CharField(null=True, max_length=200)
    phone = models.CharField(null=True, max_length=10)
    username = models.CharField(null=True, max_length=200)
    email = models.EmailField()
    profile_pic = models.FileField(upload_to='static/uploads', default='static/images/img1.jpg')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Reporter(models.Model):
    first_name = models.CharField(max_length=30, validators=[validators.MinLengthValidator(2)])
    last_name = models.CharField(max_length=30, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Article(models.Model):
    headline = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    pub_date = models.DateField(auto_now_add=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)





