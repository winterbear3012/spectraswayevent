from django.urls import path
from .views import  chatbot_response, chatbot_view

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot'),
    path("respond/", chatbot_response, name="chatbot_response"),
]
