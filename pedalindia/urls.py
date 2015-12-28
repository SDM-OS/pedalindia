from django.conf.urls import patterns, include, url
from django.contrib import admin
from events.views import EventsListView, EventDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', EventsListView.as_view(), name='home'),
    url(r"^event/(?P<slug>\w+)/$", EventDetailView.as_view(),
        name="event"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
