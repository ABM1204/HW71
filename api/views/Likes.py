from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Post, Like


class LikesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)


