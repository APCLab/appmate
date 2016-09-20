from rest_framework import routers

from app.views import *

router = routers.DefaultRouter()
router.register(r'track', TrackViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'queue_list', QueueListViewSet)
router.register(r'evaluation', EvaluationViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'driver', DriverViewSet)
