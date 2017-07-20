from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'IotViewSet',
)


class IotViewSet(viewsets.ModelViewSet):
    queryset = Iot.objects.all()
    serializer_class = IotSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = IotFilter
