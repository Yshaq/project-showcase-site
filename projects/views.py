from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Project, Review, Tag
from .forms import ProjectForm

# Create your views here.
class ProjectListView(generic.ListView):
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

def CreateProjectView(request):
    form = ProjectForm()

    if (request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('project-list')


    context = {
        'form': form,
    }

    return render(request, 'projects/project_form.html', context)

def UpdateProjectView(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=project)

    if (request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if (form.is_valid()):
            form.save()
            return redirect('project-list')


    context = {
        'form': form,
    }

    return render(request, 'projects/project_form.html', context)

def DeleteProjectView(request, id):
    project = get_object_or_404(Project, pk=id)
    if (request.method == 'POST'):
        project.delete()
        return redirect('project-list')

    context = {'project': project}
    return render(request, 'projects/delete_template.html', context)

            
