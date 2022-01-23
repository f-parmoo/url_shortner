from api.models import UrlShortner
from django.test import TestCase


class TestUrlShortner(TestCase):
    def setUp(self):
        self.url = UrlShortner.objects.create(url='https://www.google.com/')

    def test__str__(self):
        self.assertEqual('https://www.google.com/', str(self.url))



