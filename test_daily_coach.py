#!/usr/bin/env python3
"""
Test Daily Wellness Coach feature
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.services.daily_coach import DailyWellnessCoach

def test_daily_coach():
    print("Testing Daily Wellness Coach...")
    
    coach = DailyWellnessCoach()
    
    # Get today's nudges
    nudges = coach.get_daily_nudges()
    
    print(f"Date: {nudges['date']}")
    print(f"Journal Prompt: {nudges['journaling_prompt']}")
    print(f"Mindfulness: {nudges['mindfulness_activity']['name']} - {nudges['mindfulness_activity']['instructions'][:50]}...")
    print(f"Gratitude: {nudges['gratitude_prompt']}")
    
    # Test personalized message
    mood_history = [3, 4, 2, 5, 4]
    message = coach.get_personalized_message(mood_history)
    print(f"Personalized Message: {message}")
    
    print("\nDaily Wellness Coach: OK")

if __name__ == "__main__":
    test_daily_coach()