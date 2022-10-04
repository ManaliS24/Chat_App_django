from django.dispatch import receiver
from django.db.models.signals import m2m_changed, pre_save
from .models import Profile, Friend
from django.contrib.auth.models import User

@receiver(m2m_changed, sender=Profile.friends.through)
def add_friend(sender, instance, action, **kwargs):
    if action == 'pre_add' or action == 'pre_remove':
        # old_friends = Profile.objects.get(id=instance.id)
        instance.__old_friends=[]
        for friend in Profile.objects.get(pk=instance.pk).friends.all():
            instance.__old_friends.append(friend)
    elif action == 'post_add' or action == 'post_remove':
        new_friends = instance.friends.all()
        if new_friends != instance.__old_friends:
            for frend1 in new_friends:
                if frend1 not in instance.__old_friends:
                    print(frend1, " added.")
                    profile = Profile.objects.get(id=frend1.profile.id)
                    friend = Friend.objects.get(profile=instance)
                    profile.friends.add(friend)
                    profile.save()

            for frend2 in instance.__old_friends:
                if not instance.friends.filter(pk=frend2.pk):
                    print(frend2, " removed.")
                    profile = Profile.objects.get(id=frend2.profile.id)
                    friend = Friend.objects.get(profile=instance)
                    profile.friends.remove(friend)
                    profile.save()


# @receiver(pre_save, sender=Profile)
# def add_friend(sender, instance, created, **kwargs):
#     print("sender: ", sender)
#     print("instance: ", instance)
#     print("created: ", created)
#     if created:
#         pass
#         #User.objects.create(user=sender,name=sender.username)
