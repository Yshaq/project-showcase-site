from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('<int:id>/', views.userProfile, name='user-profile'),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
]