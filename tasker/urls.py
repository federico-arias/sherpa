from django.conf.urls import url
from tasker.views import *

urlpatterns = [
    url(r'^projects/$', ProjectsList.as_view(), name='projects-list'), 
    url(r'^projects/create/$', ProjectsCreate.as_view(), name='project-create'), 
    url(r'^projects/(\d+)/tasks/create/$', ProjectsTasksCreate.as_view(), name='projects-tasks-create'), 
    url(r'^projects/(\d+)/tasks/list/$', ProjectsTasksList.as_view(), name='projects-tasks-list'), 
    url(r'^tasks/(\d+)/attachment/create', TasksAttachmentsCreate.as_view(), name='task-attachment-create'),
    url(r'tasks/(?P<pk>\d+)/responsibles/update/$', TasksResponsiblesUpdate.as_view(), name='task-responsible-update'),
    url(r'^$', ProjectsList.as_view()), 
    # url(r'^tasks/([0-9]{1-3})/attachment/create/$', views.upload_attachments, name='tasks-attachment-create'), 
]
