from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile

#signals

# @reciever(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
        )

post_save.connect(createProfile, sender=User)

def deleteUser(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Profile)