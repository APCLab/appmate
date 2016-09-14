from rest_framework import routers

from app.views import *

router = routers.DefaultRouter()
router.register(r'sample', SampleViewSet)
router.register(r'demo', DemoViewSet)
