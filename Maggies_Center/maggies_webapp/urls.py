from django.conf.urls import include, url
from .views import Export, schedule, AddUser, AddVisitor, main_page
from .async_calls import get_suggestion

urlpatterns = [
		url(r'^$', main_page, name='index'),
        url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^export/', Export.as_view(), name='export'),
        url(r'^schedule/', schedule, name='schedule'),
        url(r'^add-user/', AddUser.as_view(), name="add-user"),
        url(r'^add-visitor/', AddVisitor.as_view(), name="add-visitor"),
        url(r'^get-suggestion/(?P<partial>[\w]+)/$', get_suggestion,
            name="get_suggestion")
    ]
