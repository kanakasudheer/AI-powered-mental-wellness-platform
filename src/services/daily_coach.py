from datetime import datetime
import random

class DailyWellnessCoach:
    def __init__(self):
        self.journaling_prompts = [
            "What made you smile today?",
            "Describe a challenge you overcame recently.",
            "What are you most grateful for right now?",
            "How did you show kindness to yourself today?",
            "What's one thing you learned about yourself this week?",
            "Write about a moment when you felt proud of yourself.",
            "What would you tell your younger self?",
            "Describe your ideal day. What makes it special?",
            "What's a fear you'd like to overcome?",
            "How do you want to grow in the next month?"
        ]
        
        self.mindfulness_activities = [
            {
                'name': '5-4-3-2-1 Grounding',
                'duration': '2 minutes',
                'instructions': 'Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste. Take your time with each.'
            },
            {
                'name': 'Mindful Breathing',
                'duration': '2 minutes', 
                'instructions': 'Breathe naturally. Count each breath from 1 to 10, then start over. If your mind wanders, gently return to counting.'
            },
            {
                'name': 'Body Scan',
                'duration': '2 minutes',
                'instructions': 'Close your eyes. Notice sensations from your toes to your head. Don\'t judge, just observe.'
            },
            {
                'name': 'Loving Kindness',
                'duration': '2 minutes',
                'instructions': 'Send good wishes: "May I be happy, may I be peaceful." Then extend to someone you love, then someone neutral.'
            },
            {
                'name': 'Mindful Observation',
                'duration': '2 minutes',
                'instructions': 'Pick an object nearby. Observe its color, texture, shape, weight. Notice details you never saw before.'
            }
        ]
        
        self.gratitude_prompts = [
            "Name 3 people who made your day better",
            "What's something small that brought you joy today?",
            "Think of a skill or ability you're grateful to have",
            "Recall a kind gesture someone showed you recently",
            "What's something in nature you appreciate?",
            "Name a comfort or convenience you often take for granted",
            "Think of a lesson from a difficult experience you're now grateful for",
            "What's a memory that always makes you smile?",
            "Name something about your body you're thankful for",
            "What opportunity are you grateful to have right now?"
        ]
    
    def get_daily_nudges(self):
        """Get today's personalized wellness nudges"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Use date as seed for consistent daily content
        random.seed(today)
        
        return {
            'date': today,
            'journaling_prompt': random.choice(self.journaling_prompts),
            'mindfulness_activity': random.choice(self.mindfulness_activities),
            'gratitude_prompt': random.choice(self.gratitude_prompts)
        }
    
    def display_daily_coach(self):
        """Display daily wellness coach interface"""
        import streamlit as st
        
        st.subheader("🌟 Daily AI Wellness Coach")
        st.write("*Your personalized wellness nudges for today*")
        
        nudges = self.get_daily_nudges()
        
        # Create three columns for the nudges
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📝 Journal Prompt")
            st.info(f"💭 {nudges['journaling_prompt']}")
            if st.button("✅ Completed Journaling", key="journal_done"):
                st.success("Great job! +20 points earned!")
                # Add gamification points
                from .gamification import GamificationService
                gamification = GamificationService()
                gamification.add_activity('journal')
        
        with col2:
            st.markdown("### 🧘 2-Min Mindfulness")
            activity = nudges['mindfulness_activity']
            st.info(f"🎯 **{activity['name']}** ({activity['duration']})\n\n{activity['instructions']}")
            if st.button("✅ Completed Mindfulness", key="mindful_done"):
                st.success("Wonderful! +15 points earned!")
                # Add gamification points
                from .gamification import GamificationService
                gamification = GamificationService()
                gamification.add_activity('breathing')
        
        with col3:
            st.markdown("### 🙏 Gratitude Reflection")
            st.info(f"💝 {nudges['gratitude_prompt']}")
            if st.button("✅ Reflected on Gratitude", key="gratitude_done"):
                st.success("Beautiful! +10 points earned!")
                # Add gamification points
                from .gamification import GamificationService
                gamification = GamificationService()
                gamification.add_activity('affirmation')
        
        # Daily completion tracker
        st.markdown("---")
        st.subheader("📅 Today's Wellness Progress")
        
        # Check completion status from session state
        if 'daily_completions' not in st.session_state:
            st.session_state.daily_completions = {}
        
        today_key = nudges['date']
        if today_key not in st.session_state.daily_completions:
            st.session_state.daily_completions[today_key] = {
                'journal': False,
                'mindfulness': False, 
                'gratitude': False
            }
        
        # Progress indicators
        progress_col1, progress_col2, progress_col3 = st.columns(3)
        
        with progress_col1:
            journal_status = "✅" if st.session_state.daily_completions[today_key]['journal'] else "⏳"
            st.metric("Journaling", journal_status)
        
        with progress_col2:
            mindful_status = "✅" if st.session_state.daily_completions[today_key]['mindfulness'] else "⏳"
            st.metric("Mindfulness", mindful_status)
        
        with progress_col3:
            gratitude_status = "✅" if st.session_state.daily_completions[today_key]['gratitude'] else "⏳"
            st.metric("Gratitude", gratitude_status)
        
        # Daily completion bonus
        all_complete = all(st.session_state.daily_completions[today_key].values())
        if all_complete:
            st.success("🎉 Daily Wellness Complete! Bonus +25 points!")
        else:
            remaining = sum(1 for v in st.session_state.daily_completions[today_key].values() if not v)
            st.info(f"💪 {remaining} activities remaining for today's wellness goals!")
    
    def get_personalized_message(self, mood_history=None):
        """Generate personalized coaching message based on mood"""
        if not mood_history:
            return "Ready to start your wellness journey today? 🌱"
        
        recent_avg = sum(mood_history[-7:]) / min(7, len(mood_history))
        
        if recent_avg >= 4:
            return "You've been doing great! Keep up the positive momentum!"
        elif recent_avg >= 3:
            return "You're on a steady path. Today's activities can boost your mood!"
        else:
            return "Let's focus on gentle self-care today. Small steps count!"