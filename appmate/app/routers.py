from rest_framework import routers

from app.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'concert_info', ConcertInfoViewSet)
router.register(r'concert_bid', ConcertBidViewSet)
router.register(r'ticket', TicketViewSet)
