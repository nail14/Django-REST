from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# from users.models import users
from .models import CustomUser, Book, Biography, Article


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'birthday_year', 'email']
        # fields = ('first_name', 'last_name')
        # exclude = ('first_name', 'last_name')


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.ModelSerializer):
    author = CustomUserModelSerializer()

    class Meta:
        model = Article
        exclude = ['first_name']


class BookSerializer(serializers.ModelSerializer):
    CustomUser = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

        def perform_create(self, serializer):
            serializer.save()

# author1 = CustomUser.objects.create(name='Грин', birthday_year=1880)
# serializer = CustomUserModelSerializer(CustomUser1)
# print(serializer.data) # {'id': 17, 'name': 'Грин', 'birthday_year': 1880}
# biography = Biography.objects.create(text='Некоторая биография', CustomUser=CustomUser1)
# serializer = BiographySerializer(biography)
# print(serializer.data) # {'text': 'Некоторая биография', 'author': 17}
# article = Article.objects.create(name='Некоторая статья', CustomUser=CustomUser1)
# serializer = ArticleSerializer(article)
# print(serializer.data) # {'id': 8, 'author': OrderedDict([('id', 17), ('name',
# 'Грин'), ('birthday_year', 1880)])}
# CustomUser2 = CustomUser.objects.create(name='Пушкин', birthday_year=1799)
# book = Book.objects.create(name='Некоторая книга')
# book.authors.add(CustomUser1)
# book.authors.add(CustomUser2)
# book.save()
# serializer = BookSerializer(book)
# print(serializer.data) # {'id': 9, 'authors': ['Грин', 'Пушкин'], 'name':'Некоторая книга'}


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
