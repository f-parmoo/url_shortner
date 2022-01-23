from rest_framework import serializers
from .models import UrlShortner, UrlStats


class UrlStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlStats
        fields = ['created_at']


class UrlShortnerSerializers(serializers.ModelSerializer):
    stats_serializer = UrlStatSerializer(source='stats', many=True, read_only=True)

    class Meta:
        model = UrlShortner
        fields = ['id', 'url', 'shorten_url', 'full_shorten_url', 'created_at', 'visit_count', 'stats_serializer']
        read_only_fields = ['id', 'shorten_url', 'full_shorten_url', 'created_at', 'visit_count', 'stats_serializer']

        extra_kwargs = {
            'url': {'default': 'https://www.google.com/'}
        }
