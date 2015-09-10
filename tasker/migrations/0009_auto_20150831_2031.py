# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0008_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsible',
            name='photo',
            field=models.FileField(default=b'user.png', upload_to=b'files'),
        ),
    ]
