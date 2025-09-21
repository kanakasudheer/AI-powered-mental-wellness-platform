import random
from typing import Dict, List

class WellnessContent:
    def __init__(self):
        self.affirmations = {
            'anxiety': [
                "I am safe in this moment. I can handle whatever comes my way.",
                "My anxiety does not define me. I am stronger than my fears.",
                "I breathe in calm and breathe out tension."
            ],
            'stress': [
                "I take things one step at a time. I don't need to do everything at once.",
                "I am capable and resilient. I can overcome challenges.",
                "I choose to focus on what I can control."
            ],
            'general': [
                "I am worthy of love and respect, including from myself.",
                "Every day is a new opportunity to grow and learn.",
                "I am enough, just as I am."
            ]
        }
        
        self.breathing_exercises = [
            {
                'name': '4-7-8 Breathing',
                'instructions': 'Inhale for 4 counts, hold for 7, exhale for 8. Repeat 4 times.',
                'duration': '2-3 minutes'
            },
            {
                'name': 'Box Breathing',
                'instructions': 'Inhale for 4, hold for 4, exhale for 4, hold for 4. Repeat.',
                'duration': '3-5 minutes'
            }
        ]
        
        self.journal_prompts = [
            "What are three things I'm grateful for today?",
            "What challenge did I overcome recently, and how did I do it?",
            "What would I tell a friend who was going through what I'm experiencing?",
            "What small act of kindness can I do for myself today?",
            "What is one thing I learned about myself this week?"
        ]
        
        self.mindfulness_activities = [
            {
                'name': '5-4-3-2-1 Grounding',
                'description': 'Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste'
            },
            {
                'name': 'Body Scan',
                'description': 'Focus on each part of your body from head to toe, noticing sensations'
            },
            {
                'name': 'Mindful Walking',
                'description': 'Walk slowly and focus on each step, your breathing, and surroundings'
            }
        ]
    
    def get_daily_affirmation(self, mood_type: str = 'general') -> str:
        """Get personalized daily affirmation"""
        affirmations = self.affirmations.get(mood_type, self.affirmations['general'])
        return random.choice(affirmations)
    
    def get_breathing_exercise(self) -> Dict:
        """Get a breathing exercise"""
        return random.choice(self.breathing_exercises)
    
    def get_journal_prompt(self) -> str:
        """Get a journaling prompt"""
        return random.choice(self.journal_prompts)
    
    def get_mindfulness_activity(self) -> Dict:
        """Get a mindfulness activity"""
        return random.choice(self.mindfulness_activities)
    
    def get_wellness_plan(self, mood_type: str, duration: str = 'short') -> Dict:
        """Generate personalized wellness plan"""
        plan = {
            'affirmation': self.get_daily_affirmation(mood_type),
            'breathing': self.get_breathing_exercise(),
            'mindfulness': self.get_mindfulness_activity(),
            'journal_prompt': self.get_journal_prompt()
        }
        
        if duration == 'extended':
            plan['additional_activities'] = [
                'Listen to calming music for 10 minutes',
                'Take a short walk outside',
                'Practice gentle stretching'
            ]
            
        return plan
    
    def get_crisis_resources(self) -> Dict:
        """Get mental health crisis resources"""
        return {
            'helplines': {
                'NIMHANS': '080-46110007',
                'iCALL': '9152987821',
                'Vandrevala Foundation': '9999666555'
            },
            'online_resources': [
                'https://www.nimhans.ac.in/',
                'https://www.icallhelpline.org/'
            ],
            'immediate_steps': [
                'Reach out to a trusted friend or family member',
                'Call one of the helplines above',
                'Go to the nearest hospital if in immediate danger'
            ]
        }