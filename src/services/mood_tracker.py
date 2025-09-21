from datetime import datetime, timedelta
from typing import Dict, List
import json

class MoodTracker:
    def __init__(self):
        self.mood_data = []
        self.mood_scale = {
            1: 'Very Low', 2: 'Low', 3: 'Neutral', 
            4: 'Good', 5: 'Very Good'
        }
    
    def log_mood(self, mood_score: int, notes: str = "") -> Dict:
        """Log daily mood with optional notes"""
        if mood_score < 1 or mood_score > 5:
            return {'error': 'Mood score must be between 1-5'}
            
        mood_entry = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat(),
            'mood_score': mood_score,
            'mood_label': self.mood_scale[mood_score],
            'notes': notes
        }
        
        self.mood_data.append(mood_entry)
        return {'success': True, 'entry': mood_entry}
    
    def get_mood_trends(self, days: int = 7) -> Dict:
        """Analyze mood trends over specified days"""
        if not self.mood_data:
            return {'message': 'No mood data available'}
            
        recent_data = self.mood_data[-days:] if len(self.mood_data) >= days else self.mood_data
        
        if not recent_data:
            return {'message': 'Insufficient data for analysis'}
            
        scores = [entry['mood_score'] for entry in recent_data]
        avg_mood = sum(scores) / len(scores)
        
        # Simple trend analysis
        if len(scores) >= 2:
            recent_trend = scores[-3:] if len(scores) >= 3 else scores[-2:]
            if all(recent_trend[i] <= recent_trend[i+1] for i in range(len(recent_trend)-1)):
                trend = 'improving'
            elif all(recent_trend[i] >= recent_trend[i+1] for i in range(len(recent_trend)-1)):
                trend = 'declining'
            else:
                trend = 'stable'
        else:
            trend = 'insufficient_data'
            
        return {
            'average_mood': round(avg_mood, 2),
            'trend': trend,
            'total_entries': len(recent_data),
            'recommendation': self.get_mood_recommendation(avg_mood, trend)
        }
    
    def get_mood_recommendation(self, avg_mood: float, trend: str) -> str:
        """Generate personalized recommendations based on mood patterns"""
        if avg_mood < 2.5 and trend == 'declining':
            return "Your mood has been low lately. Consider talking to someone you trust or trying some self-care activities."
        elif avg_mood < 3 and trend == 'stable':
            return "Your mood seems consistent but could use a boost. Try some mindfulness or physical activity."
        elif trend == 'improving':
            return "Great! Your mood is improving. Keep up the positive habits you've been practicing."
        else:
            return "You're doing well! Continue with your current wellness routine."
    
    def get_daily_checkin_prompt(self) -> Dict:
        """Generate personalized daily check-in questions"""
        prompts = [
            "How are you feeling today on a scale of 1-5?",
            "What's one thing you're grateful for today?",
            "How would you describe your energy level today?",
            "What emotion are you experiencing most right now?",
            "On a scale of 1-5, how supported do you feel today?"
        ]
        
        import random
        return {
            'prompt': random.choice(prompts),
            'date': datetime.now().strftime('%Y-%m-%d')
        }