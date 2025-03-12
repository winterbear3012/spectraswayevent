from django.contrib import admin
from .models import ChatbotInteraction

@admin.register(ChatbotInteraction)
class ChatbotInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'response', 'timestamp')
    search_fields = ('user__username', 'message')
    list_filter = ('timestamp',)
