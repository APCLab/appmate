from django.shortcuts import render

from rest_framework import viewsets

from app.models import Sample
from app.serializers import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
