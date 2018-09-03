from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.urls import reverse
from .forms import HomeForm
from .models import Post ,Friend
from django.contrib.auth.models import User
# Create your views here.


class HomeView(TemplateView):
   template_name = 'home/home.html'

   def get(self , request):
      form = HomeForm()
      posts = Post.objects.all().order_by('-created')
      users = User.objects.exclude(pk = request.user.pk)

      Friend.objects.get_or_create( current_user = request.user)
      friend = Friend.objects.get( current_user = request.user)
      friends = friend.users.all()

      args = {'form' : form , 'posts' : posts , 'users' : users , 'friends' : friends}
      return render(request , self.template_name , args )

   def post(self , request):

      form = HomeForm(request.POST)

      if form.is_valid:
         post =form.save(commit=False)
         post.user = request.user
         post.save()
         return redirect(reverse('home:home'))


def change_friends(request , operation , pk):
   if operation == 'add':
      current_user = request.user
      new_friend = User.objects.get(pk =pk)
      Friend.make_friend(current_user , new_friend)

   elif operation == 'remove':
      current_user = request.user
      old_friend = User.objects.get(pk =pk)
      Friend.lose_friend(current_user , old_friend)


   return redirect(reverse('home:home'))


