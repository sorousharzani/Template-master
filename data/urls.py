from django.conf.urls import url
from .views import Posts
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^post/$' , Posts.as_view() , name='posts')

]

urlpatterns = format_suffix_patterns(urlpatterns)
