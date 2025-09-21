import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        self.system_prompt = """You are MitraMind, an AI mental wellness companion for Indian youth. 
        You are empathetic, culturally sensitive, and focused on mental health support.
        
        Guidelines:
        - Be warm, understanding, and non-judgmental
        - Provide emotional support and practical wellness advice
        - If someone mentions self-harm or suicide, immediately provide crisis resources: NIMHANS (080-46110007), iCALL (9152987821)
        - Suggest breathing exercises, mindfulness, or journaling when appropriate
        - Keep responses concise but caring
        - Use culturally appropriate language for Indian context
        """
        
    def get_response(self, user_message: str, conversation_history: list = None) -> str:
        try:
            # Build context with conversation history
            context = self.system_prompt + "\n\nConversation:\n"
            
            if conversation_history:
                for msg in conversation_history[-5:]:  # Last 5 messages for context
                    role = "User" if msg["role"] == "user" else "MitraMind"
                    context += f"{role}: {msg['content']}\n"
            
            context += f"User: {user_message}\nMitraMind:"
            
            response = self.model.generate_content(context)
            return response.text
            
        except Exception as e:
            return "I'm having trouble connecting right now. Please try again or reach out to NIMHANS (080-46110007) if you need immediate support."
    
    def detect_crisis(self, message: str) -> bool:
        crisis_keywords = ['suicide', 'kill myself', 'end it all', 'no point living', 'hurt myself', 'want to die']
        return any(keyword in message.lower() for keyword in crisis_keywords)