from django.conf import settings
from django_hosts import patterns, host
host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'subdomains_tutorial.api_urls', name='api'),
)