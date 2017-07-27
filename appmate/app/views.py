from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'IotViewSet',
    'KugiViewSet',
)


class IotViewSet(viewsets.ModelViewSet):
    queryset = Iot.objects.all()
    serializer_class = IotSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = IotFilter


class KugiViewSet(viewsets.ModelViewSet):
    queryset = Kugi.objects.all()
    serializer_class = KugiSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = KugiFilter
