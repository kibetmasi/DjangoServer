from . import views
from django.urls import path
from rest_framework import routers
from .views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register('api-users', views.UserViewSet)
urlpatterns = [
    path('', views.index),
    path('api/appointments', views.ListAppointments.as_view()),
    path('api/users', views.UserView.as_view()),
    path('authenticate', CustomObtainAuthToken.as_view()),
]