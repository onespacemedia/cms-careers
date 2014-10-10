""" Models used by the jobs app """
from django.views.generic import ListView, DetailView

from .models import Job


class JobListView(ListView):
    """ A list of all Jobs """
    model = Job

    def get_paginate_by(self, queryset):
        """Returns the number of jobs to show per page."""
        return self.request.pages.current.content.per_page


class JobDetailView(DetailView):
    """ An Individual Job """
    model = Job
    slug_field = 'url_title'
    slug_url_kwarg = 'url_title'
