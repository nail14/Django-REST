from django.urls import path
from users.views import CustomUserModelViewSet

app_name = 'userapp'
urlpatterns =[
    path('', CustomUserModelViewSet.as_view()),

]