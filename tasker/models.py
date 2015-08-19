from django.db import models
from django.utils import timezone
import os
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import python_2_unicode_compatible

def get_url_for_task(taskinstance, filename):
    return os.path.join(str(taskinstance.project.pk), filename)

@python_2_unicode_compatible
class Sprint(models.Model):
    name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    total_points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=400)
    url = models.CharField(max_length=400, blank=True, null=True)

    def create_new(self):
        pass
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/projects/%i/tasks/list/" % self.pk

@python_2_unicode_compatible
class Responsible(models.Model):
    name = models.CharField(max_length=400)
    photo = models.FileField(default='user.png', upload_to='files')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TaskType(models.Model):
    name = models.CharField(max_length=400)
    order = models.IntegerField()
    effort_points = models.IntegerField()
    xsl_proc = models.CharField(blank=True, null=True, max_length=400)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Task(models.Model):
    project = models.ForeignKey('Project')
    assigned_to = models.ForeignKey('Responsible', blank=True, null=True)
    tasktype = models.ForeignKey('TaskType')

    due_date = models.DateField(blank=True, null=True)
    attached_source = models.FileField(blank=True, null=True, upload_to=get_url_for_task)
    completed_on = models.DateField(blank=True, null=True)
    assigned_on = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return "/projects/%i/tasks/list/" % self.project.pk

    def __str__(self):
        return self.name

# meeting = models.ForeignKey('Meeting')
# graphic_fields = models.ForeignKey('Meeting')

# Starschema-like
class Burndown(models.Model):
    xWeek = models.IntegerField()
    yTasksDone = models.IntegerField()
    Sprint = models.ForeignKey('Sprint')

