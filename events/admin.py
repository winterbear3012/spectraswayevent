from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'date', 'venue_type', 'attendees', 'theme', 'created_at')
    search_fields = ('event_type', 'theme')
    list_filter = ('date', 'venue_type', 'attendees')
    
