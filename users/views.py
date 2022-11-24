from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Biography, Book, Article
from .serializers import CustomUserModelSerializer, BiographySerializer, BookSerializer, ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


# class ExampleView(APIView):
#     permission_classes = [AllowAny]

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
    permission_classes = [StaffOnly]


class ArticleUserModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




