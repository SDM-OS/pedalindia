from django.conf.urls import patterns, include, url
from django.contrib import admin
from events.views import EventsListView, EventDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', EventsListView.as_view(), name='home'),
    url(r'^events/(?P<slug>[\w-]+)/$', EventDetailView.as_view(),
    name='events'),

    url(r'^admin/', include(admin.site.urls)),
)
