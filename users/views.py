from django.shortcuts import get_object_or_404, render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, id):
    profile = get_object_or_404(Profile, pk=id)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    return render(request, 'users/user-profile.html', {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills,})

def loginUser(request):
    if (request.user.is_authenticated):
        return redirect('profiles')

    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        # try:
        #     user = User.objects.get(username = username)
        # except:
        #     print('no such user')
        #     messages.error(request, 'No such user in the database')

        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'Credentials do not match')

    return render(request, 'users/login_form.html')

def logoutUser(request):
    logout(request)
    return redirect('profiles')

def registerUser(request):
    form = CustomUserCreationForm()

    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f'User {user.username} created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Form filled incorrectly')

    return render(request, 'users/register_form.html', {'form': form })