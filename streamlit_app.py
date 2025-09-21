import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.services.gemini_service import GeminiService
from src.services.mood_tracker import MoodTracker
from src.services.wellness_content import WellnessContent
from src.services.analytics_service import AnalyticsService
from src.services.study_timer import StudyTimer
from src.services.gamification import GamificationService
from src.services.daily_coach import DailyWellnessCoach

# Page config
st.set_page_config(
    page_title="MitraMind - Mental Wellness Companion",
    page_icon="🌱",
    layout="centered"
)

# Initialize services
@st.cache_resource
def init_services():
    return {
        'gemini': GeminiService(),
        'mood_tracker': MoodTracker(),
        'wellness': WellnessContent(),
        'analytics': AnalyticsService(),
        'study_timer': StudyTimer(),
        'gamification': GamificationService(),
        'daily_coach': DailyWellnessCoach()
    }

services = init_services()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mood_data" not in st.session_state:
    st.session_state.mood_data = []

# Header
st.title("🌱 MitraMind")
st.subheader("Your AI Mental Wellness Companion")
st.write("*Confidential support for Indian youth*")

# Sidebar for features
with st.sidebar:
    st.header("Wellness Tools")
    
    # Daily Coach Nudge (top of sidebar)
    daily_coach = services['daily_coach']
    nudges = daily_coach.get_daily_nudges()
    
    st.subheader("🌟 Today's Wellness")
    with st.expander("Daily Nudges", expanded=False):
        st.write(f"📝 **Journal**: {nudges['journaling_prompt'][:50]}...")
        st.write(f"🧘 **Mindful**: {nudges['mindfulness_activity']['name']}")
        st.write(f"🙏 **Gratitude**: {nudges['gratitude_prompt'][:50]}...")
        st.info("Visit Daily Coach tab for full activities!")
    
    # Gamification stats
    gamification = services['gamification']
    stats = gamification.get_user_stats()
    st.metric("Wellness Points", stats['total_points'], "🏆")
    st.metric("Mood Streak", f"{stats['mood_streak']} days", "🔥")
    
    # Mood tracking
    st.subheader("📊 Daily Mood Check")
    mood_score = st.slider("How are you feeling today?", 1, 5, 3)
    mood_notes = st.text_input("Any notes? (optional)")
    
    if st.button("Log Mood"):
        result = services['mood_tracker'].log_mood(mood_score, mood_notes)
        services['analytics'].add_mood_data(mood_score, mood_notes)
        if 'error' not in result:
            success, msg = gamification.add_activity('mood_check')
            st.success(f"Mood logged: {result['entry']['mood_label']}")
            if success:
                st.success(msg)
            st.session_state.mood_data.append(result['entry'])
    
    # Wellness activities
    st.subheader("🧘 Quick Wellness")
    
    if st.button("Daily Affirmation"):
        affirmation = services['wellness'].get_daily_affirmation()
        st.info(f"✨ {affirmation}")
        success, msg = gamification.add_activity('affirmation')
        if success:
            st.success(msg)
    
    if st.button("Breathing Exercise"):
        exercise = services['wellness'].get_breathing_exercise()
        st.info(f"🫁 **{exercise['name']}**\n\n{exercise['instructions']}")
        success, msg = gamification.add_activity('breathing')
        if success:
            st.success(msg)
    
    if st.button("Journal Prompt"):
        prompt = services['wellness'].get_journal_prompt()
        st.info(f"📝 {prompt}")
        success, msg = gamification.add_activity('journal')
        if success:
            st.success(msg)
    
    # Crisis resources
    st.subheader("🆘 Need Help?")
    if st.button("Crisis Resources"):
        st.error("**Immediate Support:**\n- NIMHANS:9914563258\n- iCALL: 7898745625\n- Vandrevala: 9999111178")

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["💬 Chat", "📊 Analytics", "📚 Study Timer", "🎮 Achievements", "🌟 Daily Coach"])

with tab1:
    st.header("💬 Chat with MitraMind")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

with tab2:
    services['analytics'].display_analytics_dashboard()

with tab3:
    services['study_timer'].display_study_timer()

with tab4:
    services['gamification'].display_wellness_streaks()

with tab5:
    services['daily_coach'].display_daily_coach()

# Chat input (outside tabs)
if prompt := st.chat_input("How are you feeling today?"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Add points for chatting
    gamification = services['gamification']
    success, msg = gamification.add_activity('chat_session')
    
    # Check for crisis
    if services['gemini'].detect_crisis(prompt):
        crisis_response = """I'm really concerned about you. Please reach out for immediate help:
        
**Crisis Helplines:**
- NIMHANS: 080-46110007
- iCALL: 9152987821
- Vandrevala Foundation: 9999666555

You matter and help is available. Please don't hesitate to call."""
        
        st.session_state.messages.append({"role": "assistant", "content": crisis_response})
    else:
        # Get AI response
        with st.spinner("MitraMind is thinking..."):
            response = services['gemini'].get_response(prompt, st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Footer
st.markdown("---")
st.caption("MitraMind is a supportive tool, not a replacement for professional mental health care.")
st.caption("If you're in crisis, please contact the helplines above or seek immediate professional help.")