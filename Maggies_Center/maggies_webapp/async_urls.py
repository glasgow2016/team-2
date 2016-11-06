from django.conf.urls import include, url
from .async_calls import get_suggestion, visitor_left

urlpatterns = [
    url('^get-suggestion/(?P<centre_id>[0-9]+)/(?P<partial>[\w]+)/$',
            get_suggestion, name="get_suggestion"),
    url('^set-left/(?P<person_id>[0-9]+)/$', visitor_left, name="visitor_left")
    ]