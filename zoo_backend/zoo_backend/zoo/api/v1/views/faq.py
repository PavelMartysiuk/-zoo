from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import FAQ
from zoo.api.v1.serializers.faq_serializer import FAQSerializer


class FAQListView(
    generics.ListAPIView,
):
    permission_classes = (AllowAny,)
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



class FAQDetailsView(
    generics.RetrieveAPIView,
):
    permission_classes = (AllowAny,)
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

