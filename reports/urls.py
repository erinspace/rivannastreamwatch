from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from reports import views

urlpatterns = [
    url(r'^$', views.ReportList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ReportDetail.as_view(), name='report-detail'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
