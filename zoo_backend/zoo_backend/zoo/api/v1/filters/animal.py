from django_filters import rest_framework as filters

from zoo.models import Animal


class AnimalFilter(filters.FilterSet):

    class Meta:
        model = Animal
        fields = ("category", )
