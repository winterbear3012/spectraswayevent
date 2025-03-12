from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forum.models import ForumPost  # Example: Importing models if needed

def base(request):
    return render(request, 'base.html')

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# AI Event Generator Page
def ai_generator(request):
    return render(request, 'ai_generator/ai_generator.html')

# Forum Home Page
def forum_home(request):
    posts = ForumPost.objects.all()  # Fetch forum posts if needed
    return render(request, 'forum/forum_home.html', {'posts': posts})

# Forum Post Detail Page
def forum_post_detail(request, slug):
    post = ForumPost.objects.get(slug=slug)
    return render(request, 'forum/forum_post_detail.html', {'post': post})

# Create Forum Post Page
@login_required
def create_forum_post(request):
    return render(request, 'forum/create_forum_post.html')

# Chatbot Page
def ai_chatbot(request):
    return render(request, 'ai_chatbot.html')

# Events Page
def event_create(request):
    return render(request, 'event_create.html')

def event_detail(request):
    return render(request, 'events/event_detail.html')

def event_edit(request):
    return render(request, 'events/event_edit.html')

def event_list(request):
    return render(request, 'events/event_list.html')

# Authentication Views
def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def logout_view(request):
    return redirect('home')  # Redirect to home after logout

