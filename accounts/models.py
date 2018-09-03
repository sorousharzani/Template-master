from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#for making queries like filtering ordering easier

class UserProfileManager(models.Manager):

    def get_queryset(self):
        queryset = super(UserProfileManager , self).get_queryset().filter(city='tehran').order_by('user')
        return  queryset

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    description = models.CharField(max_length= 100, default='', null=True ,blank=True)
    city = models.CharField(max_length= 100, default='', null=True ,blank=True)
    website = models.URLField(default='' , null=True , blank=True)
    phone_number = models.IntegerField(default='0', null=True , blank=True)
    image = models.ImageField(upload_to='profile_image' , null=True, blank=True)

    #tehran = UserProfileManager()

    def __str__(self):
        return '{}'.format(self.user)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile , sender=User)










