from django.shortcuts import render

from rest_framework import filters, viewsets

from app.filters import *
from app.models import *
from app.serializers import *

__all__ = (
    'UserViewSet',
    'RestaurantViewSet',
    'RateViewSet',
    'ThumbupViewSet',
    'MenuViewSet',
    'OrderViewSet',
    'ReservationViewSet',
    'FavoriteViewSet',
    'SensorViewSet',
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RestaurantFilter


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RateFilter


class ThumbupViewSet(viewsets.ModelViewSet):
    queryset = Thumbup.objects.all()
    serializer_class = ThumbupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ThumbupFilter


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MenuFilter


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = OrderFilter


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ReservationFilter


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FavoriteFilter


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SensorFilter
