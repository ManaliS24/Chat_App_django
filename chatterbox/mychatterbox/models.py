from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="img", blank=True, null=True)
    friends =models.ManyToManyField('Friend', related_name="my_friends")
    __old_friends=None


    def __str__(self):
        return self.name

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.__old_friends = Profile.objects.get(id=self.id)
        # self.__old_friends = self.friends.all()

    # def save(self, *args, **kwargs):
    #     print("Old: ", self.__old_friends)
    #     new_friends = self.friends.all()
    #     print("New: ", new_friends)
    #     # if self.friends != self.__original_friends:
    #     #     print("Friends added/removed.")
    #     super().save(*args, **kwargs)
    #     # self.__old_friends = self.friends.all()

class Friend(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.profile.name


class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    received_at= models.DateTimeField(null=True)

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.received_at = timezone.datetime.now()
        return super(ChatMessage, self).save(*args, **kwargs)
