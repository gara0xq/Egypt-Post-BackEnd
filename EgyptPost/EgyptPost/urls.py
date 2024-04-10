from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Authin.urls import *
from TechnicalSupport.urls import *
from Files.urls import *

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'user', UserViewSet, basename='user')
router.register(r'logout', LogoutViewSet, basename='logout')

router.register('first-devices', FirstDevicesViewSet, basename='first-devices')
router.register('second-devices', SecondDevicesViewSet, basename='second-devices')
router.register('offices', OfficesViewSet, basename='offices')
router.register('devices-module', DevicesModuleViewSet, basename='devices-module')
router.register('sector', SectorViewSet, basename='sector')

router.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('admin/', admin.site.urls),  # Use admin.site.urls directly
    path('', include(router.urls)),

]