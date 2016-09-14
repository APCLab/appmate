from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'UserViewSet',
    'ConcertInfoViewSet',
    'ConcertBidViewSet',
    'TicketViewSet',
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter


class ConcertInfoViewSet(viewsets.ModelViewSet):
    queryset = ConcertInfo.objects.all()
    serializer_class = ConcertInfoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ConcertInfoFilter


class ConcertBidViewSet(viewsets.ModelViewSet):
    queryset = ConcertBid.objects.all()
    serializer_class = ConcertBidSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ConcertBidFilter


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TicketFilter
