from django.contrib import admin

from cms.admin import SearchMetaBaseAdmin

from .models import Job


@admin.register(Job)
class JobAdmin(SearchMetaBaseAdmin):
    prepopulated_fields = {"url_title": ("title",)}

    fieldsets = (
        (None, {
            "fields": (
                "page",
                "title",
                "url_title",
                "location",
                "summary",
                "description",
                "how_to_apply"
            )
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )
