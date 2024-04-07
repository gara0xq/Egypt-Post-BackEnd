from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('auth/', include('Authin.urls')),
    path('technicalSupport/', include('TechnicalSupport.urls')),
    path('messages/', include('Files.urls')),
]