from django.views.generic import View, ListView, CreateView, DetailView, UpdateView
from .models import Project, Task
from .unit import Unidad
from django.http import FileResponse, HttpResponse
import os

class ProjectsList(ListView):
    model=Project


class ProjectsTasksCreate(CreateView):
    model=Task
    fields=('tasktype', 'due_date', 'attached_source', 'project')
    def form_valid(self, form):
         self.object = form.save(commit=False)
         self.object.project = Project.objects.filter(pk__exact=self.args[0])[0]
         self.object.save()
         return super(ProjectsTasksCreate, self).form_valid(form)

class ProjectsCreate(CreateView):
    model=Project
    fields=['name','url']


class ProjectsTasksList(ListView):
    model=Task
    template_name='tasker/project_task_list.html'
    def get_queryset(self):
        queryset = super(ProjectsTasksList, self).get_queryset()
        return queryset.filter(project=self.args[0])
    def get_context_data(self, **kwargs):
        context = super(ProjectsTasksList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ppk'] = self.args[0] 
        return context


class TasksAttachmentsCreate(View):
    def get(self, request, *args):
        xml=str(Task.objects.filter(pk__exact=self.args[0])[0].attached_source)
        u = Unidad(xml, 'minsal.xsl', self.args[0])
        fname = u.getZipFileName()
        #response = FileResponse(open(fname, 'rb'))
        response = HttpResponse(open(fname, 'rb'), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="%s"' % fname
        return response


class TasksResponsiblesUpdate(UpdateView):
    model=Task
    fields=['assigned_to',]

#class TasksGenerateProject(View):
#    pass
    #cope(request.filename)
