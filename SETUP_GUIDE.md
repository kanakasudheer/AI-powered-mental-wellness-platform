# 🌱 MitraMind Setup Guide

## Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Chatbot
**Option A: Streamlit Web Interface (Recommended)**
```bash
streamlit run streamlit_app.py
```

**Option B: Windows Batch File**
```bash
start_chatbot.bat
```

**Option C: Command Line Interface**
```bash
python main.py
```

### 3. Start Chatting!
- Open your browser to `http://localhost:8501`
- Start chatting with MitraMind
- Use sidebar tools for mood tracking and wellness activities

## Features Available

### 🤖 AI Chat
- Powered by Gemini 1.5 Flash
- Empathetic, culturally-aware responses
- Crisis detection and support

### 📊 Mood Tracking
- Daily mood logging (1-5 scale)
- Trend analysis
- Personalized recommendations

### 🧘 Wellness Tools
- Daily affirmations
- Breathing exercises
- Mindfulness activities
- Journal prompts

### 🆘 Crisis Support
- Automatic detection
- NIMHANS: 080-46110007
- iCALL: 9152987821
- Vandrevala: 9999666555

## API Configuration

The Gemini API key is already configured in `.env` file:
```
GEMINI_API_KEY=AIzaSyAna41mz8HodZH1bZ6B-okMEZKXkbEcciE
```

## Testing

Run tests to verify everything works:
```bash
python test_gemini.py    # Test Gemini API
python test_demo.py      # Test all features
```

## Troubleshooting

**Issue: Dependencies not found**
```bash
pip install streamlit google-generativeai python-dotenv
```

**Issue: API key error**
- Check `.env` file exists
- Verify API key is correct

**Issue: Port already in use**
```bash
streamlit run streamlit_app.py --server.port 8502
```

## Project Structure
```
mitramind/
├── streamlit_app.py          # Main web interface
├── src/services/
│   ├── gemini_service.py     # Gemini AI integration
│   ├── mood_tracker.py       # Mood tracking
│   └── wellness_content.py   # Wellness activities
├── .env                      # API configuration
└── requirements.txt          # Dependencies
```

---
**Ready to help Indian youth with mental wellness! 🌱**