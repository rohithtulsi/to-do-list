from dataclasses import fields
import django_filters

from base.models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['priority', 'complete']
