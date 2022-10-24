from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# from users.models import users


from .models import CustomUser


class CustomUserModelSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'birthday_year', 'email']
        # fields = ('first_name', 'last_name')
        # exclude = ('first_name', 'last_name')

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.UUIDField()
#     last_name = serializers.UUIDField()
#     birthday_year = serializers.IntegerField()
#     # phno = serializers.CharField()
#     email = serializers.CharField()
#
#     def create(self, validated_data):
#         return users.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('name', instance.name)
#         instance.birthday_year = validated_data.get('age', instance.age)
#         # instance.phno = validated_data.get('phno', instance.phno)
#         instance.last_name = validated_data.get('uname', instance.uname)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance


# class UserModelSerializer(ModelSerializer):
#
#     class Meta:
#         model = MyCustomUser
#         # fields = '__all__'
#         fields = ('username', 'first_name', 'last_name', 'birthday_year', 'email')
#         # exclude = ('first_name', 'last_name')

