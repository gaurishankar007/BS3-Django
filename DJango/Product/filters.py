import django_filters
from django_filters import CharFilter
from .models import *


class PersonFilter(django_filters.FilterSet):
    email_contains = CharFilter(field_name='email', lookup_expr='icontains')
    firstname_contains = CharFilter(field_name='firstname', lookup_expr='icontains')

    class Meta:
        model = Person
        fields = ''  # exclude = ['firstname', 'lastname', 'phone']
