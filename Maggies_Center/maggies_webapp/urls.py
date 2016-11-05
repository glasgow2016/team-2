from django.conf.urls import include, url
from .views import Export, schedule

urlpatterns = [
        url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^export/', Export.as_view(), name='export'),
        url(r'^schedule/', schedule, name='schedule'),
    ]
