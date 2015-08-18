# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='stage',
        ),
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 8, 3, 16, 33, 37, 909584, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sprint',
            name='total_points',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='responsible',
            name='photo',
            field=models.FileField(default='user.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, to='tasker.Responsible'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True),
        ),
    ]
