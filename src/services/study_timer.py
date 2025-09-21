import time
from datetime import datetime, timedelta
import streamlit as st

class StudyTimer:
    def __init__(self):
        self.session_active = False
        self.break_activities = [
            "Take 5 deep breaths",
            "Stretch your arms and neck", 
            "Look away from screen for 30 seconds",
            "Drink some water",
            "Do 10 jumping jacks",
            "Practice gratitude - think of one good thing"
        ]
    
    def start_study_session(self, duration_minutes=25):
        """Start a Pomodoro-style study session"""
        if 'study_start_time' not in st.session_state:
            st.session_state.study_start_time = datetime.now()
            st.session_state.study_duration = duration_minutes
            return True
        return False
    
    def get_session_status(self):
        """Check current study session status"""
        if 'study_start_time' not in st.session_state:
            return {'status': 'not_started', 'time_left': 0}
        
        start_time = st.session_state.study_start_time
        duration = st.session_state.study_duration
        elapsed = (datetime.now() - start_time).total_seconds() / 60
        time_left = max(0, duration - elapsed)
        
        if time_left <= 0:
            return {'status': 'break_time', 'time_left': 0}
        else:
            return {'status': 'studying', 'time_left': int(time_left)}
    
    def end_session(self):
        """End current study session"""
        if 'study_start_time' in st.session_state:
            del st.session_state.study_start_time
            del st.session_state.study_duration
    
    def get_break_activity(self):
        """Get a random wellness break activity"""
        import random
        return random.choice(self.break_activities)
    
    def display_study_timer(self):
        """Display study timer interface"""
        st.subheader("📚 Study Break Timer")
        
        status = self.get_session_status()
        
        if status['status'] == 'not_started':
            col1, col2 = st.columns(2)
            with col1:
                duration = st.selectbox("Study Duration", [15, 25, 30, 45], index=1)
            with col2:
                if st.button("Start Study Session", type="primary"):
                    self.start_study_session(duration)
                    st.rerun()
        
        elif status['status'] == 'studying':
            st.success(f"📖 Study Session Active - {status['time_left']} minutes left")
            st.progress((st.session_state.study_duration - status['time_left']) / st.session_state.study_duration)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("End Session"):
                    self.end_session()
                    st.rerun()
            with col2:
                if st.button("Refresh Timer"):
                    st.rerun()
        
        elif status['status'] == 'break_time':
            st.warning("⏰ Time for a wellness break!")
            activity = self.get_break_activity()
            st.info(f"🧘 Break Activity: {activity}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Start New Session"):
                    self.end_session()
                    st.rerun()
            with col2:
                if st.button("Finish Studying"):
                    self.end_session()
                    st.success("Great study session! 🎉")
                    st.rerun()