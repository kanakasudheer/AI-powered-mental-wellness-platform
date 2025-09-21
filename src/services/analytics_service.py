import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

class AnalyticsService:
    def __init__(self):
        self.mood_data = []
    
    def add_mood_data(self, mood_score, notes=""):
        entry = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'mood_score': mood_score,
            'notes': notes,
            'timestamp': datetime.now()
        }
        self.mood_data.append(entry)
        return entry
    
    def get_mood_chart_data(self):
        if not self.mood_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(self.mood_data)
        df['date'] = pd.to_datetime(df['date'])
        daily_avg = df.groupby('date')['mood_score'].mean().reset_index()
        return daily_avg
    
    def get_mood_stats(self):
        if not self.mood_data:
            return {'avg': 0, 'trend': 'No data', 'total_entries': 0}
        
        scores = [entry['mood_score'] for entry in self.mood_data]
        avg_mood = sum(scores) / len(scores)
        
        # Simple trend calculation
        if len(scores) >= 3:
            recent = scores[-3:]
            if recent[-1] > recent[0]:
                trend = "Improving"
            elif recent[-1] < recent[0]:
                trend = "Declining" 
            else:
                trend = "Stable"
        else:
            trend = "Building data"
            
        return {
            'avg': round(avg_mood, 1),
            'trend': trend,
            'total_entries': len(scores),
            'best_day': max(scores) if scores else 0,
            'recent_avg': round(sum(scores[-7:]) / min(7, len(scores)), 1) if scores else 0
        }
    
    def display_analytics_dashboard(self):
        st.subheader("📊 Mood Analytics Dashboard")
        
        # Get data
        chart_data = self.get_mood_chart_data()
        stats = self.get_mood_stats()
        
        if chart_data.empty:
            st.info("Start logging your mood to see analytics!")
            return
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Average Mood", f"{stats['avg']}/5")
        with col2:
            st.metric("Trend", stats['trend'])
        with col3:
            st.metric("Total Entries", stats['total_entries'])
        with col4:
            st.metric("7-Day Average", f"{stats['recent_avg']}/5")
        
        # Mood trend chart
        st.subheader("Mood Trend Over Time")
        st.line_chart(chart_data.set_index('date')['mood_score'])
        
        # Mood distribution
        st.subheader("Mood Distribution")
        mood_counts = pd.Series([entry['mood_score'] for entry in self.mood_data]).value_counts().sort_index()
        st.bar_chart(mood_counts)