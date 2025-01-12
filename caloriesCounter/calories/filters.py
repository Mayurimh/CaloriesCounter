import django_filters # type: ignore
from .models import *

class fooditemFilter(django_filters.FilterSet):
    class Meta:
        model = FoodItems
        fields = ['name']  