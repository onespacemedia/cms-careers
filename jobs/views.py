""" Models used by the jobs app """
from django.views.generic import ListView, DetailView

from .models import Job


class JobListView(ListView):
    """ A list of all Jobs """
    model = Job


class JobDetailView(DetailView):
    """ An Individual Job """
    model = Job
    slug_field = 'url_title'
    slug_url_kwarg = 'url_title'
