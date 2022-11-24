from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# from users.models import users
from project.models import Project
from .models import Project


class ProjectUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'