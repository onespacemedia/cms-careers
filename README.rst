=====
Jobs
=====

Jobs just adds a job management module to the Onespacemedia CMS, it needs
the Onespacemedia CMS to run as it uses dependencies from that app.

Quick start
-----------

1. Add "jobs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'jobs',
    )

2. Run `python manage.py migrate` to create the models.
