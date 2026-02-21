import json
import requests
from django.http import JsonResponse
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
from horilla_generics.views import HorillaView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class AskAIView(LoginRequiredMixin, HorillaView):
    template_name = "ask_ai.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_title"] = "Horilla AI"
        context['available_models'] = [
            {'id': 'gemini-3-flash-preview', 'name': 'Gemini 3 Flash Preview', 'is_premium': False},
            {'id': 'gpt-4o', 'name': 'GPT-4o (Premium)', 'is_premium': True},
            {'id': 'claude-3-5-sonnet', 'name': 'Claude 3.5 Sonnet (Premium)', 'is_premium': True},
            {'id': 'gpt-4-turbo', 'name': 'GPT-4 Turbo (Premium)', 'is_premium': True},
        ]
        return context

@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            model_id = data.get('model', 'gemini-3-flash-preview')
            
            # Fetch CRM stats for context
            stats = {
                'leads': apps.get_model('leads', 'Lead').objects.count() if apps.is_installed('horilla_crm.leads') else 0,
                'accounts': apps.get_model('accounts', 'Account').objects.count() if apps.is_installed('horilla_crm.accounts') else 0,
                'contacts': apps.get_model('contacts', 'Contact').objects.count() if apps.is_installed('horilla_crm.contacts') else 0,
            }

            if model_id == 'gemini-3-flash-preview':
                # Dynamically use the model name provided by the user
                # Preview models usually require v1beta
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={settings.GEMINI_API_KEY}"
                
                prompt = f"""
                You are Horilla AI, a specialized assistant for Horilla CRM.
                Current CRM State:
                - Leads: {stats['leads']}
                - Accounts: {stats['accounts']}
                - Contacts: {stats['contacts']}
                
                User Request: {message}
                
                Please provide a helpful, professional response in the context of Horilla CRM. 
                If the user asks about system data, use the stats provided above.
                Keep it concise and business-focused.
                """
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                response = requests.post(url, json=payload, timeout=20)
                res_data = response.json()
                
                if response.status_code == 200:
                    response_text = res_data['candidates'][0]['content']['parts'][0]['text']
                else:
                    error_msg = res_data.get('error', {}).get('message', 'Unknown API Error')
                    response_text = f"API Error: {error_msg}"
            else:
                # Mock response for premium models (shouldn't be reached if UI logic works)
                response_text = f"The {model_id} model is currently in mock mode. Please switch to Gemini for real updates."

            return JsonResponse({'status': 'success', 'response': response_text, 'model': model_id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
