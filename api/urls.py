from django.urls import path
from .views.views import Post, PostView
from .views.Likes import LikesView

urlpatterns = [
    path('posts/', PostView.as_view(), name='posts'),
    path('post/<int:pk>/', PostView.as_view(), name='post_datail_view'),
    path('like/<int:pk>/like/', LikesView.as_view(), name='post_like'),
    path('like/<int:pk>/like/unlike/', LikesView.as_view(), name='post_unlike'),
]