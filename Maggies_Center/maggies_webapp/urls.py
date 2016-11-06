from django.conf.urls import include, url
from .views import Export, Schedule, AddUser, AddVisitor, main_page,DeleteSchedule,ShowSchedule


urlpatterns = [
		url(r'^$', main_page, name='index'),
        url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^export/', Export.as_view(), name='export'),
        url(r'^schedule/', Schedule.as_view(), name='schedule'),
        url(r'^delactivity/', DeleteSchedule.as_view(), name='delschedule'),
        url(r'^add-user/', AddUser.as_view(), name="add-user"),
        url(r'^add-visitor/', AddVisitor.as_view(), name="add-visitor"),
        url(r'^async/', include("maggies_webapp.async_urls")),
        url(r'^show/(?P<slug>[0-9]+)/$',ShowSchedule.as_view(),name='show'),
    ]
