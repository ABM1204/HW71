from rest_framework import serializers
from webapp.models import Like, Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at')
        read_only_fields = ('user', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True, source='likes.count')

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at']
