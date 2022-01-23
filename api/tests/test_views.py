from django.test import TestCase
from rest_framework import status
from api.models import UrlShortner


class TestTestRunRequestAPIView(TestCase):

    def setUp(self) -> None:
        self.url_shortner = UrlShortner.objects.create(url='https://www.google.com/')
        self.url = '/tier/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertGreaterEqual(1, len(response.json()))
