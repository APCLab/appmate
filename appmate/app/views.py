from django.shortcuts import render

from rest_framework import filters, viewsets

from app.models import Sample, SAMPLE_FIELDS
from app.serializers import SampleSerializer

SAMPLE_FILTER_FIELDS = list(SAMPLE_FIELDS)
SAMPLE_FILTER_FIELDS.remove('img')


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = SAMPLE_FILTER_FIELDS
