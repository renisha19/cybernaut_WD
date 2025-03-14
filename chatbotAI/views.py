from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .dialogflow_api import get_dialogflow_response

def chatbot_ui(request):
    """Render chatbot frontend."""
    return render(request, "chatbot.html")

@csrf_exempt
def chatbot_view(request):
    """Handle chatbot messages via Dialogflow."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            if not user_message:
                return JsonResponse({'error': 'Empty message'}, status=400)

            bot_reply = get_dialogflow_response(user_message)
            return JsonResponse({'reply': bot_reply})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
