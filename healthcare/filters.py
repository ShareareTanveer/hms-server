from django_filters import rest_framework as filters
from .models import Department, Doctor


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = ['status']


# class DoctorFilter(filters.FilterSet):
#     email = filters.CharFilter(field_name="category__title", lookup_expr='icontains')
#     first_name = filters.CharFilter(field_name="tags__tag__name", lookup_expr='icontains')

#     class Meta:
#         model = Doctor
#         fields = ['category','email','tags']
