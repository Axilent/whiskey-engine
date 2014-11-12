from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.contrib import admin

urlpatterns = patterns('whiskeyengine.views',
    (r'^$','home'),
    (r'^related/(?P<whiskey_id>\d+)/$','related_whiskey'),
    (r'^review/(?P<whiskey_id>\d+)/$','review_whiskey'),
    (r'^recommended/$','recommended_whiskey'),
    (r'^search/$','search'),
    (r'^about-whiskeyengine/$','about_whiskey_engine'),
    (r'^about-whiskey/$','about_american_whiskey'),
    (r'^whiskey/(?P<whiskey_slug>[-\w]+)/$','home'),
)


# ===================
# = For development =
# ===================
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()