"""
Definition of urls for TheoWebsite.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from TheoWebsite.views import hello, current_datetime, hours_ahead

urlpatterns = [
    # Examples:
    # url(r'^$', TheoWebsite.views.home, name='home'),
    # url(r'^TheoWebsite/', include('TheoWebsite.TheoWebsite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', hello),
]
