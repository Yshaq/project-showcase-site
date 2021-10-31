from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('<int:id>/', views.userProfile, name='user-profile'),
]