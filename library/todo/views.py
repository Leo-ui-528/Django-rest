from rest_framework.viewsets import ModelViewSet
from .models import TodoList
from .serializers import TodoModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoModelSerializer
