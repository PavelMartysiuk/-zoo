from rest_framework import serializers

from zoo.models import Animal


class AnimalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ("id", "name", "photo", "type")
