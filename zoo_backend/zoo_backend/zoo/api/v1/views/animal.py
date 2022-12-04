from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import Animal
from zoo.api.v1.serializers.animal_serializer import AnimalDetailsSerializer, AnimalListSerializer
from zoo.api.v1.filters.animal import AnimalFilter

from django_filters.rest_framework import DjangoFilterBackend


class AnimalListView(
    generics.ListAPIView,
):
    permission_classes = (AllowAny,)
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter


class AnimalDetailsView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailsSerializer
