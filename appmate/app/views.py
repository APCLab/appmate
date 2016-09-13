from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import SampleFilter
from app.models import Sample, SAMPLE_FIELDS
from app.serializers import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SampleFilter
