from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ForumPost, Comment
from .forms import ForumPostForm, CommentForm

# Forum Homepage - List of Posts
def forum_home(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'posts': posts})

# View a Single Forum Post & Comments
def forum_post_detail(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('forum_post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'forum/forum_post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# Create a New Forum Post
@login_required
def create_forum_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post has been created successfully.")
            return redirect('forum_home')
    else:
        form = ForumPostForm()
    return render(request, 'forum/forum_create.html', {'form': form})
