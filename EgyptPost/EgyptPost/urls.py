from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('admin/', admin.site.urls, basename='admin')
router.register('auth/', include('Authin.urls'), basename='auth')
router.register('technicalSupport/', include('TechnicalSupport.urls'), basename='technicalSupport')
router.register('messages/', include('Files.urls'), basename='messages')

urlpatterns = [
    path('', include(router.urls))
]