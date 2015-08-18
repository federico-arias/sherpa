# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burndown',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('xWeek', models.IntegerField()),
                ('yTasksDone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('stage', models.TextField()),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=400)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('due_date', models.DateField()),
                ('completition_file', models.FileField(blank=True, upload_to='')),
                ('completed_on', models.DateField(blank=True)),
                ('assigned_on', models.DateField(blank=True)),
                ('assigned_to', models.ForeignKey(to='tasker.Responsible')),
                ('project', models.ForeignKey(to='tasker.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=400)),
                ('order', models.IntegerField()),
                ('effort_points', models.IntegerField()),
                ('xsl_proc', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tasktype',
            field=models.ForeignKey(to='tasker.TaskType'),
        ),
        migrations.AddField(
            model_name='burndown',
            name='Sprint',
            field=models.ForeignKey(to='tasker.Sprint'),
        ),
    ]
