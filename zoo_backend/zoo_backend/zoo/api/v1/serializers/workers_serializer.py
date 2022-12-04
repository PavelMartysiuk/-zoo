from rest_framework import serializers

from zoo.models import Worker


class WorkersDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        exclude = ("description",)
