
from destinations.views import RegisterAPI,LoginAPI
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


urlpatterns = [
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    # path('index/',index),
    # path('people/',people),
    # path('login/',login),
    # path('peopleAPI/',peopleAPI.as_view()),
    # path('',include(router.urls))
]
