from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import Category
from zoo.api.v1.serializers.category_serializer import CategorySerializer
from zoo.api.v1.filters.category import CategoryFilter

from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(
    generics.ListAPIView,
):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter



class CategoryDetailsView(
    generics.RetrieveAPIView,
):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
