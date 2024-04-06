from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register/', RegisterView.as_view(), basename='register')
router.register('login/', LoginView.as_view(), basename='login')
router.register('user/', UserView.as_view(), basename='user')
router.register('logout/', LogoutView.as_view(), basename='logout')

urlpatterns = [
    path('', include(router.urls))
]