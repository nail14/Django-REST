from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectUserModelSerializer


class ProjectUserModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectUserModelSerializer