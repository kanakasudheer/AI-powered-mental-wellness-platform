import json
import random
from datetime import datetime
from typing import Dict, List, Tuple

class AICompanion:
    def __init__(self):
        self.conversation_history = []
        self.crisis_keywords = ['suicide', 'kill myself', 'end it all', 'no point living', 'hurt myself']
        self.wellness_responses = {
            'anxiety': [
                "I understand you're feeling anxious. Let's try a quick breathing exercise together.",
                "Anxiety can feel overwhelming. Would you like to try some grounding techniques?",
                "It's okay to feel anxious. You're not alone in this."
            ],
            'stress': [
                "Stress is tough. Let's break down what's bothering you into smaller parts.",
                "I hear you're stressed. Sometimes talking through it helps. What's weighing on you?",
                "Stress affects us all. Would you like some relaxation techniques?"
            ],
            'sad': [
                "I'm here with you. It's okay to feel sad sometimes.",
                "Your feelings are valid. Would you like to talk about what's making you sad?",
                "Sadness is part of being human. You don't have to face it alone."
            ]
        }
        
    def analyze_sentiment(self, message: str) -> Dict:
        """Simple sentiment analysis using keyword matching"""
        message_lower = message.lower()
        
        # Crisis detection
        if any(keyword in message_lower for keyword in self.crisis_keywords):
            return {'sentiment': 'crisis', 'confidence': 0.9}
            
        # Emotion detection
        emotions = {
            'anxiety': ['anxious', 'worried', 'nervous', 'panic', 'scared'],
            'stress': ['stressed', 'pressure', 'overwhelmed', 'exam', 'deadline'],
            'sad': ['sad', 'depressed', 'lonely', 'hopeless', 'down'],
            'happy': ['happy', 'good', 'great', 'excited', 'joy']
        }
        
        for emotion, keywords in emotions.items():
            if any(keyword in message_lower for keyword in keywords):
                return {'sentiment': emotion, 'confidence': 0.7}
                
        return {'sentiment': 'neutral', 'confidence': 0.5}
    
    def generate_response(self, user_message: str) -> Dict:
        """Generate empathetic AI response"""
        sentiment_analysis = self.analyze_sentiment(user_message)
        
        # Crisis intervention
        if sentiment_analysis['sentiment'] == 'crisis':
            return {
                'response': "I'm really concerned about you. Please reach out to NIMHANS helpline: 6304174835 or iCALL: 9547854787. You matter and help is available.",
                'type': 'crisis',
                'resources': ['NIMHANS: 6304174835', 'iCALL: 9547854787']
            }
        
        # Empathetic responses based on emotion
        emotion = sentiment_analysis['sentiment']
        if emotion in self.wellness_responses:
            response = random.choice(self.wellness_responses[emotion])
            return {
                'response': response,
                'type': 'supportive',
                'suggested_activities': self.get_wellness_activities(emotion)
            }
        
        # Default supportive response
        return {
            'response': "I'm here to listen. How are you feeling today?",
            'type': 'general',
            'suggested_activities': ['breathing_exercise', 'gratitude_journal']
        }
    
    def get_wellness_activities(self, emotion: str) -> List[str]:
        """Get personalized wellness activities"""
        activities = {
            'anxiety': ['breathing_exercise', 'grounding_technique', 'mindfulness'],
            'stress': ['meditation', 'journaling', 'music_therapy'],
            'sad': ['gratitude_journal', 'self_compassion', 'gentle_movement']
        }
        return activities.get(emotion, ['breathing_exercise'])
    
    def chat(self, user_message: str) -> Dict:
        """Main chat interface"""
        timestamp = datetime.now().isoformat()
        
        # Store conversation
        self.conversation_history.append({
            'timestamp': timestamp,
            'user': user_message,
            'type': 'user_input'
        })
        
        # Generate AI response
        ai_response = self.generate_response(user_message)
        
        self.conversation_history.append({
            'timestamp': timestamp,
            'ai': ai_response,
            'type': 'ai_response'
        })
        
        return ai_response