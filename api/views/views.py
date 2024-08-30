from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostSerializer
from webapp.models import Post


class PostView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            post = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            updated_post = serializer.save()
            return Response(PostSerializer(updated_post).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










