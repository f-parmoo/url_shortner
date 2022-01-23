from django.shortcuts import redirect
from rest_framework import viewsets
from .models import UrlShortner, UrlStats
from .serializers import UrlShortnerSerializers


class UrlShortnerViewset(viewsets.ModelViewSet):
    queryset = UrlShortner.objects.all()
    serializer_class = UrlShortnerSerializers
    http_method_names = ['get', 'post']
    lookup_field = 'shorten_url'

    def retrieve(self, request, shorten_url, *args, **kwargs):
        url = UrlShortner.objects.get(shorten_url=shorten_url)
        UrlStats.objects.create(url=url)
        return redirect(url.url)
