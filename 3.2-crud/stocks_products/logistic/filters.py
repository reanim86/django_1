from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from logistic.models import Stock


class StockFilterSet(FilterSet):
    championship = NumberFilter(field_name='positions__product')

    class Meta:
        model = Stock
        fields = ['products']