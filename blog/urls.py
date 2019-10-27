from django.urls import path
from .views import *

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('user/<username>',UserPostListView.as_view(), name='user-posts'),
    path('post/<pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new',PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('about/',about, name='blog-about')
]
