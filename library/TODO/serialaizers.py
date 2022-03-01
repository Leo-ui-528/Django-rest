from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoList


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'