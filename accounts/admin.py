from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user' , 'full_name' ,'city' , 'phone_number' ,)

    def full_name(self , obj):
        return "{} {}".format(obj.user.first_name , obj.user.last_name)

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin , self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    full_name.short_description = 'Full Name'

admin.site.register(UserProfile , UserProfileAdmin )
