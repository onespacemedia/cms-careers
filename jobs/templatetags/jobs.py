from django.template import Library

register = Library()


@register.inclusion_tag("jobs/includes/job_list.html", takes_context=True)
def job_list(context, job_list):

    return {
        'job_list': job_list
    }
