from rest_framework.viewsets import ModelViewSet
from .models import TodoList
from .serialaizers import AuthorModelSerializer


class todo(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = AuthorModelSerializer