from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import About
from zoo.api.v1.serializers.about_serializer import AboutSerializer

class AboutListView(
    generics.ListAPIView
):
    permission_classes = (AllowAny,)
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutDetailsView(
    generics.RetrieveAPIView
):
    permission_classes = (AllowAny,)
    queryset = About.objects.all()
    serializer_class = AboutSerializer
