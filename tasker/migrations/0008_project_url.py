# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0007_auto_20150812_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(null=True, max_length=400, blank=True),
        ),
    ]
