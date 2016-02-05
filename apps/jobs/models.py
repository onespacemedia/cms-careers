import watson
from cms.apps.pages.models import ContentBase
from cms.models import HtmlField, SearchMetaBase
from django.db import models


class Jobs(ContentBase):

    """ A base for Jobs """

    # The heading that the admin places this content under.
    classifier = "apps"

    # The urlconf used to power this content's views.
    urlconf = "{{ project_name }}.apps.jobs.urls"

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        "jobs per page",
        default=5,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.__str__()


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
        return self.page.page.reverse('job', kwargs={
            'url_title': self.url_title,
        })

watson.register(Job)
