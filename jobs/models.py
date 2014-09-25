from cms.apps.pages.models import ContentBase
from django.db import models

from cms.models import SearchMetaBase, HtmlField

import watson


class Jobs(ContentBase):

    # The urlconf used to power this content's views.
    urlconf = "jobs.urls"

    standfirst = models.TextField(
        blank=True,
        null=True
    )


class Job(SearchMetaBase):

    page = models.ForeignKey(
        Jobs
    )

    title = models.CharField(
        max_length=256,
    )

    url_title = models.CharField(
        max_length=256,
        unique=True
    )

    location = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    summary = models.TextField(
        blank=True,
        null=True
    )

    description = HtmlField()

    how_to_apply = HtmlField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "{}{}/".format(
            self.page.page.get_absolute_url(),
            self.url_title
        )


watson.register(Job)
