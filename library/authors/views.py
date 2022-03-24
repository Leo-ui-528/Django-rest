from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, ArticleModelSerializer, BiographyModelSerializer, BookModelSerializer, \
    SimpleAuthorModelSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import mixins


class AuthorApiView(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def change_password(self, request):
        pass

    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    # renderer_classes = [JSONRenderer]
    # queryset = Author.objects.all()
    # serializer_class = AuthorModelSerializer

    # def get(self, request):
    #     authors = Author.objects.all()
    #     serializer = SimpleAuthorModelSerializer(authors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     return Response('post')


class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name']
    # def get_queryset(self):
    #     param = self.request.query_param['param'][0]
    #     return Author.objects.filter(first_name__contains='S')


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer
