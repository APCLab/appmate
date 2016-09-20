from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'TrackViewSet',
    'VehicleViewSet',
    'QueueListViewSet',
    'EvaluationViewSet',
    'CustomerViewSet',
    'DriverViewSet',
)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TrackFilter


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = VehicleFilter


class QueueListViewSet(viewsets.ModelViewSet):
    queryset = QueueList.objects.all()
    serializer_class = QueueListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = QueueListFilter


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EvaluationFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CustomerFilter


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DriverFilter
