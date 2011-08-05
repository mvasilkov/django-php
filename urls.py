from django.conf.urls.defaults import patterns, include, url
import main

urlpatterns = patterns(None,
    url(r'^$', main.home, name='home'),
    url(r'^phpinfo/$', main.phpinfo, name='phpinfo'),
)
