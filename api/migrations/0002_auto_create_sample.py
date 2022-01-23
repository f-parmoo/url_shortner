from django.db import migrations
from api.models import UrlShortner


def clear_data(apps, _):
    UrlShortner.objects.all().delete()


def init_data(apps, _):
    sample_urls = (
        'https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit',
        'https://www.django-rest-framework.org/api-guide/authentication/#apache-mod_wsgi-specific-configuration',
        'https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#browsing-the-api',
        'https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset',
        'https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#making-sure-our-url-patterns-are-named',
        'https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#creating-an-endpoint-for-the-highlighted-snippets')

    for url in sample_urls:
        if len(UrlShortner.objects.filter(url=url)) == 0:
            UrlShortner.objects.create(url=url)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_data, reverse_code=clear_data)

    ]
