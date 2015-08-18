# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0005_auto_20150811_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(null=True, to='tasker.Responsible', blank=True),
        ),
    ]
