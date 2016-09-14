from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'SampleViewSet',
    'DemoViewSet',
)


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SampleFilter


class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DemoFilter
