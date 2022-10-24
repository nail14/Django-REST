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
