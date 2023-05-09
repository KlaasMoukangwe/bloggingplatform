from django.urls import path
from .views import (PostListView, PostCreateView, PostDetailView, 
                    PostUpdateView, PostDeleteView, CommentCreateView,
                    LikeCreateView)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='post_comment'),
    path('post/<int:pk>/like/', LikeCreateView.as_view(), name='post_like'),
]
