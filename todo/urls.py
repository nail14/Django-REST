"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from graphene_django.views import GraphQLView

from project.views import ProjectUserModelViewSet
from users.views import CustomUserModelViewSet, BookUserModelViewSet, ArticleUserModelViewSet, BiographyUserModelViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='v1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@amail.ru"),
        license=openapi.License(name="MIT License"),

    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('books', BookUserModelViewSet)
router.register('biography', BiographyUserModelViewSet)
router.register('articles', ArticleUserModelViewSet)
router.register('project', ProjectUserModelViewSet)
# router.register('book', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/project', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/<str:version>/users/', CustomUserModelViewSet.as_view()),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/users/v1', include('userapp.urls', namespace='v1')),
    # path('api/users/v2', include('userapp.urls', namespace='v2')),
    # path('swagger<str:format>/', schema_view.without_ui()),
    # path('swagger/', schema_view.with_ui('swagger')),
    # path('redoc/', schema_view.with_ui('redoc')),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

    path('', TemplateView.as_view(template_name='index.html')),



    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    # schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    # name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
    # name='schema-redoc'),
]

