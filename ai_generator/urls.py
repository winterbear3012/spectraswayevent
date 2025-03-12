from django.urls import path
from .views import ai_generator

urlpatterns = [
    path('ai_generator', ai_generator, name='ai_generator'),
]
