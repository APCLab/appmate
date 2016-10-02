from rest_framework import routers

from app.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'restaurant', RestaurantViewSet)
router.register(r'rate', RateViewSet)
router.register(r'thumbup', ThumbupViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'order', OrderViewSet)
router.register(r'reservation', ReservationViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'sensor', SensorViewSet)
