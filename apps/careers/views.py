from django.views.generic import DetailView, ListView

from .models import Career


class CareerListView(ListView):
    model = Career

    def get_paginate_by(self, queryset):
        return self.request.pages.current.content.per_page


class CareerDetailView(DetailView):
    model = Career
    slug_field = 'url_title'
    slug_url_kwarg = 'url_title'
