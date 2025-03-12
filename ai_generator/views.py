from django.shortcuts import render
import random  # Used to generate random AI event ideas

def ai_generator(request):
    event_ideas = [
        "A futuristic tech-themed party 🚀",
        "A cozy winter wonderland wedding ❄️",
        "A superhero cosplay convention 🦸",
        "A music festival with global artists 🎶",
        "A retro 80s disco night 💃"
        "Outdoor Beach Wedding with Sunset Theme",
        "Royal Palace Wedding with Gold Decor",
        "Garden Party Birthday with Fairy Lights",
        "Music Concert with Celebrity Appearance",
        "Corporate Event with Full Tech Setup",
        "Destination Wedding in Mountains",
        "Pool Party with Neon Theme",
        "Retro Bollywood Theme Sangeet Night",
        "Luxury Anniversary Party on Cruise"
    ]
    selected_idea = random.choice(event_ideas)  # Selects a random event idea
    return render(request, 'ai_generator/ai_generator.html', {'event_idea': selected_idea})
