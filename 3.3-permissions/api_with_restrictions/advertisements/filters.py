from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Описываем какие поля могут фильтроваться, поле дата создания можно указывать в формате от/до/меньше/больше"""
    created_at = DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
