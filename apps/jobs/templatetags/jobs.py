""" Template tags used by the jobs module. """
from django.template import Library

from ..models import Job

register = Library()


@register.inclusion_tag("jobs/includes/job_list.html")
def job_list():
    """Returns a list of all jobs

    Returns:
        list of all Job objects
    """

    return {
        'job_list': Job.objects.all()
    }
