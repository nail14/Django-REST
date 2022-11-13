from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):  # AbstractBaseUser, PermissionsMixin
    # username = ASCIIUsernameValidator()
    # class Meta:
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    birthday_year = models.PositiveIntegerField(verbose_name="День рождения", blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)

    def __str__(self):
        return f'{self.last_name}-{self.first_name}'


class Biography(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(CustomUser)


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(CustomUser, models.PROTECT)