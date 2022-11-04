import django_filters
from base.models import Task


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['priority', 'complete']
