from django import forms
from .models import Event

class EventForm(forms.ModelForm):
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

    event_type = forms.ChoiceField(choices=EVENT_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    venue_type = forms.ChoiceField(choices=VENUE_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    attendees = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    theme = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['event_type', 'description', 'date', 'venue_type', 'attendees', 'theme']
