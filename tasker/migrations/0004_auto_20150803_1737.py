# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0003_auto_20150803_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsible',
            name='photo',
            field=models.FileField(upload_to='files', default='user.jpg'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_on',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_on',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='completition_file',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
