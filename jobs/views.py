from django.views.generic import ListView, DetailView

from .models import Job


class JobListView(ListView):
    model = Job


class JobDetailView(DetailView):
    model = Job
    slug_field = 'url_title'
    slug_url_kwarg = 'url_title'
