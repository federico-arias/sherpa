# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0004_auto_20150803_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completition_file',
            new_name='attached_source',
        ),
    ]
