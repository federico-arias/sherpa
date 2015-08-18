# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tasker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0006_auto_20150811_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attached_source',
            field=models.FileField(blank=True, null=True, upload_to=tasker.models.get_url_for_task),
        ),
    ]
