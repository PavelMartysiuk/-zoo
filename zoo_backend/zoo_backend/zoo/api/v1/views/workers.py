from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from zoo.models import Worker
from zoo.api.v1.serializers.workers_serializer import WorkersDetailsSerializer, WorkerListSerializer


class WorkersListView(
    generics.ListAPIView,

):
    permission_classes = (AllowAny,)
    queryset = Worker.objects.all()
    serializer_class = WorkerListSerializer


class WorkersDetailsView(
    generics.RetrieveAPIView,

):
    permission_classes = (AllowAny,)
    queryset = Worker.objects.all()
    serializer_class = WorkersDetailsSerializer
