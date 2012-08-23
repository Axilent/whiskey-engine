from django.conf.urls.defaults import *

urlpatterns = patterns('mobilewhiskey.views',
    (r'^$','home'),
    (r'^blend/$','blend'),
    (r'^search/$','search'),
    (r'^whiskey/(?P<whiskey_slug>[-\w]+)/$','home'),
)