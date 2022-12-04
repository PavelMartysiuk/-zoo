from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import Country
from zoo.api.v1.serializers.country_serializer import CountrySerializer




class CountryListView(
    generics.ListAPIView,

):
    permission_classes = (AllowAny,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class CountryDetailsView(
    generics.RetrieveAPIView,

):
    permission_classes = (AllowAny,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
