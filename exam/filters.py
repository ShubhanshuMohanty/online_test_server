import django_filters
from .models import McqQuestion

class McqQuestionFilter(django_filters.FilterSet):
    batch = django_filters.CharFilter(field_name='batch__batch_name', lookup_expr='iexact')
    exam_name = django_filters.CharFilter(field_name='exam_name__course_name', lookup_expr='iexact')
    test_name = django_filters.CharFilter(field_name='test_name__name', lookup_expr='iexact')

    class Meta:
        model = McqQuestion
        fields = ['batch', 'exam_name', 'test_name']
