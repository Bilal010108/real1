from django_filters import FilterSet
from itertools import product

from django_filters.rest_framework import FilterSet
from  .models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact',],
            'have':['exact',],
            'price':['gt','lt' ]
        }