from django.conf.urls import include, url
from .async_calls import get_suggestion

urlpatterns = [
    url('^get-suggestion/(?P<centre_id>[0-9]+)/(?P<partial>[\w]+)/$',
            get_suggestion, name="get_suggestion")
    ]