from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserFullModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

