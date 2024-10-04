# chatbot/views.py
from django.http import JsonResponse
from transformers import pipeline

# Cargar el modelo de lenguaje
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

conversation_history = []  # Para mantener un historial de la conversación

def chat(request):
    user_input = request.GET.get('message')

    # Agregar la entrada del usuario al historial
    conversation_history.append(f"Usuario: {user_input}")

    # Formatear el historial como un solo string
    input_text = "\n".join(conversation_history)

    # Generar una respuesta
    response = chatbot(input_text, max_length=150, num_return_sequences=1)[0]['generated_text']

    # Agregar la respuesta al historial
    conversation_history.append(f"Bot: {response}")

    return JsonResponse({"response": response})


