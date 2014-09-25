from django.template import Library

from jobs.models import Job

register = Library()


@register.inclusion_tag("jobs/includes/job_list.html")
def job_list():

    return {
        'job_list': Job.objects.all()
    }
