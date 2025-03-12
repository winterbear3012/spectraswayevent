from django.urls import path
from .views import forum_home, forum_post_detail, create_forum_post

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('post/<slug:slug>/', forum_post_detail, name='forum_post_detail'),
    path('create/', create_forum_post, name='create_forum_post'),
]
