from django.shortcuts import render , redirect
from .forms import (
    RegistrationForm ,
    EditProfileForm  ,
                    )
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import inlineformset_factory



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))

    else :
        form = RegistrationForm()
        args = {'form' : form}
        return render(request , 'accounts/reg_form.html' , args)

def view_profile(request , pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user' :user}
    return  render(request , 'accounts/profile.html' , args)



def edit_profile(request):
    #for
    profile_in_line_formset = inlineformset_factory(User, UserProfile, fields=('city',
            'website',
            'phone_number', 'image',))


    if request.method == 'POST':
        form = EditProfileForm(request.POST ,request.FILES, instance=request.user)
        formset = profile_in_line_formset(request.POST ,request.FILES, instance=request.user)
        if form.is_valid():
            edited_user = form.save(commit=False)
            formset = profile_in_line_formset(request.POST ,request.FILES, instance=edited_user)
            if formset.is_valid():
                edited_user.save()
                formset.save()
                return redirect(reverse('accounts:view_profile'))

    else:
        formset = profile_in_line_formset(instance=request.user)
        form = EditProfileForm(instance=request.user)
        args = {'form' : form , 'formset' : formset }
        return render(request , 'accounts/profile_edit.html' , args)




def change_password(request):
    if request.method == 'POST' :
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts: change_password'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form}
        return  render(request , 'accounts/change_password.html' , args)

