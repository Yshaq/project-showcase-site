from django.shortcuts import render
from django.views import generic
from .models import Project, Review, Tag

# Create your views here.
class ProjectListView(generic.ListView):
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
            
