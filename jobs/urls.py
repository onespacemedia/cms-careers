""" URLs used by the jobs app """
from django.conf.urls import patterns, url

from .views import JobListView, JobDetailView

urlpatterns = patterns(
    "",
    url(r"^$", JobListView.as_view(), name='job_list'),
    url(r"^(?P<url_title>[a-z-]+)/$", JobDetailView.as_view(), name='job'),
)
