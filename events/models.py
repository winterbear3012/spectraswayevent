from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('corporate', 'Corporate'),
        ('conference', 'Conference'),
        ('concert', 'Concert'),
        ('other', 'Other'),
    ]

    VENUE_TYPES = [
        ('banquet hall', 'Banquet Hall'),
        ('conference center', 'Conference Center'),
        ('hotels/resorts', 'Hotels/Resorts'),
        ('restaurant', 'Restaurant'),
        ('outdoor spaces', 'Outdoor Spaces'),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField()
    date = models.DateTimeField()
    venue_type = models.CharField(max_length=30, choices=VENUE_TYPES)
    attendees = models.PositiveIntegerField()
    theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.date.strftime('%Y-%m-%d')}"
