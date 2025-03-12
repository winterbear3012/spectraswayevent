from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Simple Logic (Chatbot Response)

        responses = {
                "hello": "Hi there! How can I help you?",
                "how are you": "I'm just a bot, but I'm doing great!",
                "bye": "Goodbye! Have a great day!",
                "who are you": "I'm an AI chatbot created to assist you."
            }
        
        if "plan event" in user_message.lower():
            response = "Great! What type of event do you want to plan?"
        elif "wedding" in user_message.lower():
            response = "Nice! How many guests are you expecting?"
        elif "venue" in user_message.lower():
            response = "Would you like an indoor or outdoor venue?"
        elif "date" in user_message.lower():
            response = "What date are you planning your event?"
        else:
            response = "I can help you plan an event. Ask me anything."

        return JsonResponse({"response": response})



