from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Biography, Book, Article
from .serializers import CustomUserModelSerializer, BiographySerializer, BookSerializer, ArticleSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer

    # def get_queryset(self):
    #     return CustomUser.objects.get(id=1)


class BiographyUserModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookUserModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleUserModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




