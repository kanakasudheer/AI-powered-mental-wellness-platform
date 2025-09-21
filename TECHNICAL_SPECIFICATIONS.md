# 🌱 MitraMind - Technical Specifications

## **System Requirements**

### **Minimum Hardware Requirements**
- **CPU**: 2-core processor (Intel i3 or equivalent)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB free space
- **Network**: Internet connection for AI API calls
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### **Software Dependencies**
```
Python 3.11+
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
pandas>=1.5.0
```

---

## **Architecture Specifications**

### **System Architecture Pattern**
- **Pattern**: Microservices Architecture with Service-Oriented Design
- **Frontend**: Single Page Application (SPA) using Streamlit
- **Backend**: Python-based service layer with modular components
- **Communication**: RESTful API calls and direct function invocation
- **Data Flow**: Unidirectional data flow with session state management

### **Component Architecture**
```
┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           Streamlit Web Interface                       │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐              │ │
│  │  │Chat │ │Anal.│ │Timer│ │Game │ │Coach│              │ │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘              │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Service Layer                            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │GeminiService│ │MoodTracker  │ │Analytics    │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │StudyTimer   │ │Gamification │ │DailyCoach   │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │Session State│ │Gemini API   │ │Local Storage│          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

---

## **API Specifications**

### **Google Gemini API Integration**
```python
# API Configuration
API_ENDPOINT: https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash
METHOD: POST
AUTHENTICATION: API Key (Bearer Token)
RATE_LIMIT: 60 requests/minute
MAX_TOKENS: 8192 input, 8192 output
```

### **Request/Response Format**
```json
// Request
{
  "contents": [
    {
      "parts": [
        {
          "text": "User message with context"
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 1024
  }
}

// Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "AI response text"
          }
        ]
      }
    }
  ]
}
```

---

## **Database Schema**

### **Session State Structure**
```python
# In-Memory Data Models
session_state = {
    "messages": [
        {
            "role": "user|assistant",
            "content": "string",
            "timestamp": "ISO datetime"
        }
    ],
    "mood_data": [
        {
            "date": "YYYY-MM-DD",
            "mood_score": "1-5 integer",
            "notes": "string",
            "timestamp": "ISO datetime"
        }
    ],
    "wellness_stats": {
        "total_points": "integer",
        "mood_streak": "integer",
        "last_mood_date": "YYYY-MM-DD",
        "activities_today": ["activity_type_date"],
        "total_activities": "integer",
        "level": "integer"
    },
    "study_sessions": [
        {
            "start_time": "ISO datetime",
            "duration": "minutes integer",
            "completed": "boolean"
        }
    ]
}
```

---

## **Security Specifications**

### **Data Privacy & Protection**
- **Encryption**: HTTPS/TLS 1.3 for all API communications
- **API Security**: Environment variable-based API key management
- **Data Retention**: Session-based storage, no persistent user data
- **Privacy by Design**: Local-first processing when possible

### **Crisis Safety Protocols**
```python
# Crisis Detection Algorithm
CRISIS_KEYWORDS = [
    'suicide', 'kill myself', 'end it all', 
    'no point living', 'hurt myself', 'want to die'
]

def detect_crisis(message: str) -> bool:
    return any(keyword in message.lower() for keyword in CRISIS_KEYWORDS)

# Immediate Response Protocol
if crisis_detected:
    return {
        'type': 'crisis',
        'response': 'Crisis intervention message',
        'resources': ['NIMHANS: 080-46110007', 'iCALL: 9152987821']
    }
```

---

## **Performance Specifications**

### **Response Time Requirements**
- **Chat Response**: < 3 seconds for AI generation
- **UI Interactions**: < 500ms for local operations
- **Page Load**: < 2 seconds initial load
- **Analytics Generation**: < 1 second for chart rendering

### **Scalability Metrics**
- **Concurrent Users**: 100+ simultaneous sessions (local deployment)
- **Memory Usage**: < 512MB per user session
- **API Rate Limits**: 60 requests/minute per user
- **Storage Growth**: Minimal (session-based, no persistence)

### **Optimization Strategies**
```python
# Caching Strategy
@st.cache_resource
def init_services():
    # Service initialization cached across sessions
    
@st.cache_data
def get_mood_analytics(mood_data):
    # Analytics computation cached by data hash
    
# Session State Optimization
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    # Initialize only once per session
```

---

## **Integration Specifications**

### **External Service Integration**
```python
# Gemini AI Service
class GeminiService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.system_prompt = "Cultural context for Indian youth..."
    
    def get_response(self, message: str, history: list) -> str:
        # Context-aware response generation
```

### **Crisis Helpline Integration**
```python
# Indian Mental Health Resources
CRISIS_RESOURCES = {
    'helplines': {
        'NIMHANS': '080-46110007',
        'iCALL': '9152987821', 
        'Vandrevala Foundation': '9999666555'
    },
    'online_resources': [
        'https://www.nimhans.ac.in/',
        'https://www.icallhelpline.org/'
    ]
}
```

---

## **Deployment Specifications**

### **Local Development Setup**
```bash
# Environment Setup
python -m venv mitramind_env
source mitramind_env/bin/activate  # Linux/Mac
mitramind_env\Scripts\activate     # Windows

# Dependency Installation
pip install -r requirements.txt

# Environment Configuration
echo "GEMINI_API_KEY=your_api_key" > .env

# Application Launch
streamlit run streamlit_app.py
```

### **Production Deployment Options**

#### **Option 1: Streamlit Cloud**
```yaml
# .streamlit/config.toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

#### **Option 2: Docker Containerization**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]
```

#### **Option 3: Cloud Platform (Heroku/AWS/GCP)**
```yaml
# app.yaml (Google App Engine)
runtime: python311
service: mitramind

env_variables:
  GEMINI_API_KEY: "your_api_key"

automatic_scaling:
  min_instances: 1
  max_instances: 10
```

---

## **Testing Specifications**

### **Unit Testing Framework**
```python
# test_services.py
import unittest
from src.services.mood_tracker import MoodTracker

class TestMoodTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = MoodTracker()
    
    def test_mood_logging(self):
        result = self.tracker.log_mood(4, "Good day")
        self.assertIn('success', result)
        self.assertEqual(result['entry']['mood_score'], 4)
    
    def test_trend_analysis(self):
        # Add test mood data
        for score in [3, 4, 5, 4, 5]:
            self.tracker.log_mood(score)
        
        trends = self.tracker.get_mood_trends()
        self.assertEqual(trends['trend'], 'improving')
```

### **Integration Testing**
```python
# test_integration.py
def test_crisis_detection_flow():
    gemini_service = GeminiService()
    crisis_message = "I want to hurt myself"
    
    # Test crisis detection
    is_crisis = gemini_service.detect_crisis(crisis_message)
    assert is_crisis == True
    
    # Test crisis response
    response = gemini_service.get_response(crisis_message)
    assert "NIMHANS" in response
    assert "080-46110007" in response
```

---

## **Monitoring & Analytics**

### **Application Metrics**
- **User Engagement**: Session duration, feature usage frequency
- **AI Performance**: Response time, conversation quality
- **Crisis Interventions**: Detection accuracy, resource provision
- **Wellness Impact**: Mood trend improvements, habit formation

### **Error Handling & Logging**
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Error handling example
try:
    response = gemini_service.get_response(user_message)
except Exception as e:
    logging.error(f"AI service error: {e}")
    response = "I'm having trouble connecting. Please try again or contact support."
```

---

## **Compliance & Standards**

### **Mental Health Standards**
- **Crisis Intervention**: Immediate professional resource provision
- **Privacy Protection**: No persistent storage of sensitive conversations
- **Cultural Sensitivity**: Indian context-aware AI responses
- **Professional Boundaries**: Clear limitations and referral protocols

### **Technical Standards**
- **Code Quality**: PEP 8 Python style guidelines
- **Documentation**: Comprehensive inline and external documentation
- **Version Control**: Git-based development with semantic versioning
- **Security**: OWASP security guidelines for web applications

This technical specification provides the complete blueprint for implementing, deploying, and maintaining the MitraMind platform. 🌱