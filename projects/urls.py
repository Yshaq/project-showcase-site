from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('create/', views.CreateProjectView, name='create-project'),
    path('update/<int:id>', views.UpdateProjectView, name='update-project'),
    path('delete/<int:id>', views.DeleteProjectView, name = 'delete-project'),
]