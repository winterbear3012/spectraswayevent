from django.contrib import admin
from .models import ForumPost, Comment, Category

class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ['category', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ['content']
    list_filter = ['created_at']

admin.site.register(Category)
admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(Comment, CommentAdmin)
