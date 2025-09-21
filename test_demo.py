#!/usr/bin/env python3
"""
Demo script to showcase MitraMind functionality
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.services.ai_companion import AICompanion
from src.services.mood_tracker import MoodTracker
from src.services.wellness_content import WellnessContent

def demo_ai_companion():
    """Demonstrate AI companion functionality"""
    print("AI Companion Demo")
    print("=" * 30)
    
    companion = AICompanion()
    
    # Test different scenarios
    test_messages = [
        "I'm feeling really anxious about my exams",
        "I'm so stressed with all the pressure",
        "I feel like giving up on everything",
        "I'm having a good day today"
    ]
    
    for message in test_messages:
        print(f"\nUser: {message}")
        response = companion.chat(message)
        print(f"MitraMind: {response['response']}")
        
        if 'suggested_activities' in response:
            print(f"Suggested: {', '.join(response['suggested_activities'])}")

def demo_mood_tracker():
    """Demonstrate mood tracking functionality"""
    print("\n\nMood Tracker Demo")
    print("=" * 30)
    
    tracker = MoodTracker()
    
    # Simulate mood entries
    moods = [3, 2, 4, 3, 5, 2, 4]
    notes = ["Okay day", "Stressed about work", "Good day!", "Normal", "Great day!", "Feeling low", "Better today"]
    
    for i, (mood, note) in enumerate(zip(moods, notes)):
        result = tracker.log_mood(mood, note)
        print(f"Day {i+1}: Mood {mood}/5 - {note}")
    
    # Show trends
    trends = tracker.get_mood_trends()
    print(f"\nAnalysis:")
    print(f"Average Mood: {trends['average_mood']}/5")
    print(f"Trend: {trends['trend'].title()}")
    print(f"Recommendation: {trends['recommendation']}")

def demo_wellness_content():
    """Demonstrate wellness content functionality"""
    print("\n\nWellness Content Demo")
    print("=" * 30)
    
    wellness = WellnessContent()
    
    # Show different content types
    print(f"Daily Affirmation: {wellness.get_daily_affirmation('anxiety')}")
    
    exercise = wellness.get_breathing_exercise()
    print(f"\nBreathing Exercise: {exercise['name']}")
    print(f"Instructions: {exercise['instructions']}")
    
    activity = wellness.get_mindfulness_activity()
    print(f"\nMindfulness: {activity['name']}")
    print(f"Description: {activity['description']}")
    
    print(f"\nJournal Prompt: {wellness.get_journal_prompt()}")

def main():
    """Run all demos"""
    print("MitraMind - Feature Demonstration")
    print("=" * 50)
    
    demo_ai_companion()
    demo_mood_tracker()
    demo_wellness_content()
    
    print("\n\nDemo Complete!")
    print("Run 'python main.py' to start the interactive chat interface.")

if __name__ == "__main__":
    main()