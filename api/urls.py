from rest_framework import routers
from .views import UrlShortnerViewset
from django.urls import path, include

shorten_url_routers = routers.DefaultRouter()
shorten_url_routers.register('', UrlShortnerViewset)

urlpatterns = [
    path('', include(shorten_url_routers.urls))

]
