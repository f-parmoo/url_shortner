from django.db import models
import string
import random
from django.conf import settings


class TimeTracking(models.Model):
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    class Meta:
        abstract = True


class UrlShortner(TimeTracking):
    url = models.URLField(unique=True)
    shorten_url = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.url

    def calculate_new_url(self):
        return ''.join([random.choice(string.ascii_letters) for _ in range(10)])

    def save(self, *args, **kwargs):
        while True:
            try:
                self.shorten_url = self.calculate_new_url()
                super(UrlShortner, self).save(*args, **kwargs)
                break
            except:
                pass

    @property
    def full_shorten_url(self):
        return settings.API_URL + self.shorten_url

    @property
    def visit_count(self):
        return len(self.stats.all())


class UrlStats(TimeTracking):
    url = models.ForeignKey(UrlShortner, on_delete=models.CASCADE, related_name='stats')
