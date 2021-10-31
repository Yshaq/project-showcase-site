from django.shortcuts import get_object_or_404, render
from .models import Profile

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