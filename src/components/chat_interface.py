from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.ai_companion import AICompanion
from services.mood_tracker import MoodTracker
from services.wellness_content import WellnessContent

class ChatInterface:
    def __init__(self):
        self.ai_companion = AICompanion()
        self.mood_tracker = MoodTracker()
        self.wellness_content = WellnessContent()
        self.session_active = True
        
    def display_welcome(self):
        """Display welcome message"""
        print("\nWelcome to MitraMind - Your Mental Wellness Companion")
        print("=" * 50)
        print("I'm here to listen and support you. Everything we discuss is confidential.")
        print("Type 'mood' to track your mood, 'wellness' for activities, or 'quit' to exit.")
        print("=" * 50)
        
    def display_menu(self):
        """Display available options"""
        print("\nAvailable Commands:")
        print("- Just chat with me naturally")
        print("- 'mood' - Track your daily mood")
        print("- 'wellness' - Get wellness activities")
        print("- 'trends' - View your mood trends")
        print("- 'resources' - Crisis support resources")
        print("- 'quit' - Exit MitraMind")
        
    def handle_mood_tracking(self):
        """Handle mood tracking interaction"""
        print("\nDaily Mood Check-in")
        prompt = self.mood_tracker.get_daily_checkin_prompt()
        print(f"Question: {prompt['prompt']}")
        
        try:
            mood_input = input("\nRate your mood (1-5): ").strip()
            mood_score = int(mood_input)
            
            notes = input("Any notes about your mood today? (optional): ").strip()
            
            result = self.mood_tracker.log_mood(mood_score, notes)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Mood logged: {result['entry']['mood_label']}")
                
                # Provide supportive response based on mood
                if mood_score <= 2:
                    print("\nI notice you're having a tough day. That's okay - you're not alone.")
                    wellness_plan = self.wellness_content.get_wellness_plan('stress')
                    print(f"Try this affirmation: {wellness_plan['affirmation']}")
                    
        except ValueError:
            print("Please enter a number between 1-5")
            
    def handle_wellness_activities(self):
        """Handle wellness activities"""
        print("\nWellness Activities")
        print("1. Daily Affirmation")
        print("2. Breathing Exercise") 
        print("3. Mindfulness Activity")
        print("4. Journal Prompt")
        print("5. Complete Wellness Plan")
        
        choice = input("\nChoose an activity (1-5): ").strip()
        
        if choice == '1':
            affirmation = self.wellness_content.get_daily_affirmation()
            print(f"\nToday's Affirmation: {affirmation}")
        elif choice == '2':
            exercise = self.wellness_content.get_breathing_exercise()
            print(f"\n{exercise['name']}")
            print(f"Instructions: {exercise['instructions']}")
            print(f"Duration: {exercise['duration']}")
        elif choice == '3':
            activity = self.wellness_content.get_mindfulness_activity()
            print(f"\n{activity['name']}")
            print(f"Description: {activity['description']}")
        elif choice == '4':
            prompt = self.wellness_content.get_journal_prompt()
            print(f"\nJournal Prompt: {prompt}")
        elif choice == '5':
            plan = self.wellness_content.get_wellness_plan('general')
            print(f"\nYour Wellness Plan:")
            print(f"Affirmation: {plan['affirmation']}")
            print(f"Breathing: {plan['breathing']['name']} - {plan['breathing']['instructions']}")
            print(f"Mindfulness: {plan['mindfulness']['name']} - {plan['mindfulness']['description']}")
            print(f"Journal: {plan['journal_prompt']}")
            
    def handle_mood_trends(self):
        """Display mood trends"""
        trends = self.mood_tracker.get_mood_trends()
        print(f"\nYour Mood Trends (Last 7 days)")
        
        if 'message' in trends:
            print(f"Note: {trends['message']}")
        else:
            print(f"Average Mood: {trends['average_mood']}/5")
            print(f"Trend: {trends['trend'].title()}")
            print(f"Total Entries: {trends['total_entries']}")
            print(f"\nRecommendation: {trends['recommendation']}")
            
    def handle_crisis_resources(self):
        """Display crisis resources"""
        resources = self.wellness_content.get_crisis_resources()
        print("\nMental Health Support Resources")
        print("=" * 40)
        print("Helplines:")
        for name, number in resources['helplines'].items():
            print(f"  - {name}: {number}")
            
        print("\nOnline Resources:")
        for resource in resources['online_resources']:
            print(f"  - {resource}")
            
        print("\nImmediate Steps:")
        for step in resources['immediate_steps']:
            print(f"  - {step}")
            
    def chat_loop(self):
        """Main chat interaction loop"""
        while self.session_active:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nTake care! Remember, you're stronger than you think. Come back anytime.")
                self.session_active = False
                break
                
            elif user_input.lower() == 'mood':
                self.handle_mood_tracking()
                
            elif user_input.lower() == 'wellness':
                self.handle_wellness_activities()
                
            elif user_input.lower() == 'trends':
                self.handle_mood_trends()
                
            elif user_input.lower() == 'resources':
                self.handle_crisis_resources()
                
            elif user_input.lower() == 'help':
                self.display_menu()
                
            else:
                # Regular AI chat
                response = self.ai_companion.chat(user_input)
                print(f"\nMitraMind: {response['response']}")
                
                # Show suggested activities if available
                if 'suggested_activities' in response:
                    print(f"\nSuggested activities: {', '.join(response['suggested_activities'])}")
                    
                # Show resources for crisis situations
                if response['type'] == 'crisis':
                    print("\nAdditional Resources:")
                    for resource in response['resources']:
                        print(f"  - {resource}")
                        
    def run(self):
        """Start the chat interface"""
        self.display_welcome()
        self.display_menu()
        self.chat_loop()