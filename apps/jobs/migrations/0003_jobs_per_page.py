# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20140925_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='per_page',
            field=models.IntegerField(default=5, null=True, verbose_name=b'jobs per page', blank=True),
            preserve_default=True,
        ),
    ]
