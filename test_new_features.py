#!/usr/bin/env python3
"""
Test new features: Analytics, Study Timer, Gamification
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.services.analytics_service import AnalyticsService
from src.services.study_timer import StudyTimer
from src.services.gamification import GamificationService

def test_analytics():
    print("Testing Analytics Service...")
    analytics = AnalyticsService()
    
    # Add sample mood data
    analytics.add_mood_data(4, "Good day")
    analytics.add_mood_data(3, "Okay day")
    analytics.add_mood_data(5, "Great day!")
    
    stats = analytics.get_mood_stats()
    print(f"Average mood: {stats['avg']}/5")
    print(f"Trend: {stats['trend']}")
    print("Analytics: OK")

def test_study_timer():
    print("\nTesting Study Timer...")
    timer = StudyTimer()
    
    # Test timer functionality
    timer.start_study_session(25)
    status = timer.get_session_status()
    print(f"Session status: {status['status']}")
    
    activity = timer.get_break_activity()
    print(f"Break activity: {activity}")
    print("Study Timer: OK")

def test_gamification():
    print("\nTesting Gamification...")
    
    # Mock streamlit session state
    class MockSessionState:
        def __init__(self):
            self.data = {}
        def __contains__(self, key):
            return key in self.data
        def __getitem__(self, key):
            return self.data[key]
        def __setitem__(self, key, value):
            self.data[key] = value
    
    # Mock streamlit module
    import types
    st_mock = types.ModuleType('streamlit')
    st_mock.session_state = MockSessionState()
    sys.modules['streamlit'] = st_mock
    
    gamification = GamificationService()
    
    # Test adding activities
    success, msg = gamification.add_activity('mood_check')
    print(f"Mood check: {success} - {msg}")
    
    success, msg = gamification.add_activity('breathing')
    print(f"Breathing: {success} - {msg}")
    
    stats = gamification.get_user_stats()
    print(f"Total points: {stats['total_points']}")
    print(f"Level: {stats['level']}")
    print("Gamification: OK")

def main():
    print("Testing New MitraMind Features")
    print("=" * 40)
    
    test_analytics()
    test_study_timer()
    test_gamification()
    
    print("\nAll new features working!")
    print("Run 'streamlit run streamlit_app.py' to see them in action.")

if __name__ == "__main__":
    main()