from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.api.serializers import PostSerializer

class PostApiView(APIView):
    def get(self, request):
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=posts.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)