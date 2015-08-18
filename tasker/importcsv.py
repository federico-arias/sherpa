from django.db import models
import sys, os, csv, datetime
from tasker.models import Responsible, Sprint, Project, TaskType

path = os.path.realpath('.') + '/tasktype.csv'

with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            # start = row[1].split('/')
            # end = row[2].split('/')
            _, created = TaskType.objects.get_or_create(
                name=row[0],
                order=row[1],
                effort_points=row[2],
                xsl_proc=row[3],
                #start_date = datetime.date(int(end[2]), int(end[1]), int(end[0])),
                #end_date = datetime.date(int(start[2]), int(start[1]), int(start[0])),
                )

            # creates a tuple of the new object or
            # current object and a boolean of if it was created
