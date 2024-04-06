from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('first-devices', FirstDevicesViewSet, basename='first-devices')
router.register('second-devices', SecondDevicesViewSet, basename='second-devices')
router.register('offices', OfficesViewSet, basename='offices')
router.register('devices-module', DevicesModuleViewSet, basename='devices-module')
router.register('sector', SectorViewSet, basename='sector')

urlpatterns = [
    path('', include(router.urls))
]