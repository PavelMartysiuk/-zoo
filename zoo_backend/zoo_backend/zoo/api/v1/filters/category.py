from django_filters import rest_framework as filters

from zoo.models import Category


class CategoryFilter(filters.FilterSet):

    class Meta:
        model = Category
        fields = ("id", )
