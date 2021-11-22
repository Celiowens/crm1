import django_filters

from .models import*

class OrderFiter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'