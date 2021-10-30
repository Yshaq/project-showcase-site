from django.db.models.base import Model
from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'tags', 'demo_link', 'source_link']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }