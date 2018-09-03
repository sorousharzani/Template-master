from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User , related_name='users')
    post = models.CharField(max_length=1000 , blank=True , null=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.user)


class Friend(models.Model):
    users = models.ManyToManyField(User , related_name='friends')
    current_user = models.ForeignKey(User , related_name='owner' , null=True)

    @classmethod
    def make_friend(cls , current_user , new_friend):
        friend , created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, old_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(old_friend)

    def __str__(self):
        return "{} ".format(self.current_user)


