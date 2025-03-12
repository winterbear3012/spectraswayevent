from django.db import models
from django.conf import settings

class AIGeneratedEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    generated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Links to the user who generated it
    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
