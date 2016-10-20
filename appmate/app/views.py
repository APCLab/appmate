from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'VoiceLogViewSet',
)


class VoiceLogViewSet(viewsets.ModelViewSet):
    queryset = VoiceLog.objects.all()
    serializer_class = VoiceLogSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = VoiceLogFilter
