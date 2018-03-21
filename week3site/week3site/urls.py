"""
Definition of urls for week3site.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from week3_app import views


urlpatterns = [
    # Examples:
    # url(r'^$', week3site.views.home, name='home'),
    # url(r'^week3site/', include('week3site.week3site.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', views.hello),
     url(r'^order/?$', views.order),
     url(r'^Week4/?$', views.Week4),
     url(r'^template/?$', views.template),
     url(r'^template_example/?$', views.template_example),

]
