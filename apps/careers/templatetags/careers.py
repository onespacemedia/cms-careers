from django.template import Library

from ..models import Career

register = Library()


@register.inclusion_tag("careers/includes/career_list.html")
def career_list():
    return {
        'career_list': Career.objects.all()
    }
