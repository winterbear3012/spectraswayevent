"""
URL configuration for spectraswayevent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home,about, contact, ai_generator, forum_home, forum_post_detail, create_forum_post, ai_chatbot, event_create, event_detail, event_list, event_edit, login_view, register_view, logout_view

admin.site.site_header = "Spectrasway Event Admin"
admin.site.site_title = " Spectrasway Event Admin Portal"
admin.site.index_title = "Welcome to Spectrasway Event "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('ai_generator/', ai_generator, name='ai_generator'),
    path('forum/forum_home/', forum_home, name='forum_home'),
    path('forum/post/<slug:slug>/', forum_post_detail, name='forum_post_detail'),
    path('forum/create/', create_forum_post, name='create_forum_post'),
    path('ai_chatbot/', ai_chatbot, name='ai_chatbot'),
    path('event_create/', event_create, name='event_create'),
    path('event_detail/', event_detail, name='event_detail'),
    path('event_edit/', event_edit, name='event_edit'),
    path('event_list/', event_list, name='event_list'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
