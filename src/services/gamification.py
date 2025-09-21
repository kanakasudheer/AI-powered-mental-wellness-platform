from datetime import datetime, timedelta

class GamificationService:
    def __init__(self):
        self.activities = {
            'mood_check': {'points': 10, 'name': 'Daily Mood Check'},
            'chat_session': {'points': 5, 'name': 'Chat with MitraMind'},
            'chat': {'points': 5, 'name': 'Chat with MitraMind'},
            'breathing': {'points': 15, 'name': 'Breathing Exercise'},
            'affirmation': {'points': 10, 'name': 'Daily Affirmation'},
            'journal': {'points': 20, 'name': 'Journaling'},
            'study_session': {'points': 25, 'name': 'Study Session Complete'}
        }
        
    def get_user_stats(self):
        """Get user wellness statistics from session state"""
        import streamlit as st
        
        if 'wellness_stats' not in st.session_state:
            st.session_state.wellness_stats = {
                'total_points': 0,
                'mood_streak': 0,
                'last_mood_date': None,
                'activities_today': [],
                'total_activities': 0,
                'level': 1
            }
        
        return st.session_state.wellness_stats
    
    def add_activity(self, activity_type):
        """Add points for completed activity"""
        import streamlit as st
        
        stats = self.get_user_stats()
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Check if already done today
        if f"{activity_type}_{today}" in stats['activities_today']:
            return False, "Already completed today!"
        
        # Add points and track activity
        points = self.activities[activity_type]['points']
        stats['total_points'] += points
        stats['activities_today'].append(f"{activity_type}_{today}")
        stats['total_activities'] += 1
        
        # Update level (every 100 points = new level)
        stats['level'] = (stats['total_points'] // 100) + 1
        
        # Update mood streak
        if activity_type == 'mood_check':
            self.update_mood_streak(stats)
        
        st.session_state.wellness_stats = stats
        return True, f"+{points} points earned!"
    
    def update_mood_streak(self, stats):
        """Update mood check streak"""
        today = datetime.now().date()
        last_date = stats['last_mood_date']
        
        if last_date is None:
            stats['mood_streak'] = 1
        elif isinstance(last_date, str):
            last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
            
        if last_date and (today - last_date).days == 1:
            stats['mood_streak'] += 1
        elif last_date and (today - last_date).days > 1:
            stats['mood_streak'] = 1
            
        stats['last_mood_date'] = today.strftime('%Y-%m-%d')
    
    def get_level_info(self, level):
        """Get level information and next milestone"""
        level_names = {
            1: "Wellness Beginner 🌱",
            2: "Mindful Explorer 🧭", 
            3: "Wellness Warrior 💪",
            4: "Zen Master 🧘",
            5: "Mental Health Champion 🏆"
        }
        
        name = level_names.get(level, f"Wellness Legend Lv.{level} ⭐")
        next_points = level * 100
        
        return {
            'name': name,
            'next_milestone': next_points,
            'progress_to_next': next_points - (level - 1) * 100
        }
    
    def display_wellness_streaks(self):
        """Display gamification dashboard"""
        import streamlit as st
        
        st.subheader("🎮 Wellness Streaks & Achievements")
        
        stats = self.get_user_stats()
        level_info = self.get_level_info(stats['level'])
        
        # Display main stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Points", stats['total_points'], "🏆")
        
        with col2:
            st.metric("Current Level", stats['level'], level_info['name'])
        
        with col3:
            st.metric("Mood Streak", f"{stats['mood_streak']} days", "🔥")
        
        with col4:
            st.metric("Activities Done", stats['total_activities'], "✅")
        
        # Progress to next level
        current_level_points = (stats['level'] - 1) * 100
        points_in_level = stats['total_points'] - current_level_points
        progress = points_in_level / 100
        
        st.subheader(f"Progress to Level {stats['level'] + 1}")
        st.progress(progress)
        st.caption(f"{points_in_level}/100 points in current level")
        
        # Today's activities
        today = datetime.now().strftime('%Y-%m-%d')
        today_activities = [act for act in stats['activities_today'] if today in act]
        
        st.subheader("Today's Wellness Activities")
        if today_activities:
            for activity in today_activities:
                activity_type = activity.split('_')[0]
                if activity_type in self.activities:
                    activity_name = self.activities[activity_type]['name']
                    st.success(f"✅ {activity_name}")
        else:
            st.info("No activities completed today. Start with a mood check!")
        
        # Achievement badges
        self.display_achievements(stats)
    
    def display_achievements(self, stats):
        """Display achievement badges"""
        import streamlit as st
        
        st.subheader("🏅 Achievements")
        
        achievements = []
        
        # Mood streak achievements
        if stats['mood_streak'] >= 7:
            achievements.append("🔥 Week Warrior - 7 day mood streak!")
        if stats['mood_streak'] >= 30:
            achievements.append("🌟 Monthly Master - 30 day mood streak!")
        
        # Points achievements  
        if stats['total_points'] >= 100:
            achievements.append("💯 Century Club - 100+ points!")
        if stats['total_points'] >= 500:
            achievements.append("🚀 Point Powerhouse - 500+ points!")
        
        # Activity achievements
        if stats['total_activities'] >= 10:
            achievements.append("🎯 Activity Ace - 10+ activities!")
        if stats['total_activities'] >= 50:
            achievements.append("⭐ Wellness Superstar - 50+ activities!")
        
        if achievements:
            for achievement in achievements:
                st.success(achievement)
        else:
            st.info("Complete activities to unlock achievements! 🎖️")