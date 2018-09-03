from rest_framework import serializers
from accounts.models import User
from home.models import Post ,Friend


class PostSerializers(serializers.ModelSerializer):

    class Meta :
        model = Post
        fields = (
            'user',
            'post',
            'created',
        )
