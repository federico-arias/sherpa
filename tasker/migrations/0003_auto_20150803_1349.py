# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_auto_20150803_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='total_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
