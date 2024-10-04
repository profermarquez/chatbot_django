# app.py
import gradio as gr
import requests

def send_message(message):
    response = requests.get(f'http://127.0.0.1:8000/chatbot/chat/?message={message}')
    return response.json()['response']

iface = gr.Interface(fn=send_message, 
                     inputs="text", 
                     outputs="text", 
                     title="Chatbot", 
                     description="Escribe tu mensaje para chatear con el bot.")

if __name__ == "__main__":
    iface.launch()
