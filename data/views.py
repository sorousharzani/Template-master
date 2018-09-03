from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers
from home.models import Post



class Posts(APIView):

    def get(self , request):
        posts = Post.objects.all().filter(user = request.user)
        serializer = PostSerializers(posts , many=True)
        return Response(serializer.data)

    def post(self , request):
        pass
