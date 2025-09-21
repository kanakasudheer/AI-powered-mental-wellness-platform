# 🚀 MitraMind Deployment Guide

## **Option 1: Streamlit Cloud (Recommended - Free)**

### **Steps:**
1. **Go to** [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with GitHub account
3. **Click "New app"**
4. **Select repository**: `kanakasudheer/AI-powered-mental-wellness-platform`
5. **Main file path**: `streamlit_app.py`
6. **Add secrets** in Advanced settings:
   ```
   GEMINI_API_KEY = "AIzaSyAna41mz8HodZH1bZ6B-okMEZKXkbEcciE"
   ```
7. **Click "Deploy"**

### **Your app will be live at:**
`https://mitramind-ai-wellness.streamlit.app`

---

## **Option 2: Heroku (Free Tier)**

### **Setup Files:**
```bash
# Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Create runtime.txt
echo "python-3.11.0" > runtime.txt
```

### **Deploy Steps:**
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create mitramind-wellness

# Set environment variable
heroku config:set GEMINI_API_KEY=AIzaSyAna41mz8HodZH1bZ6B-okMEZKXkbEcciE

# Deploy
git push heroku main
```

---

## **Option 3: Railway (Simple)**

### **Steps:**
1. **Go to** [railway.app](https://railway.app)
2. **Connect GitHub** repository
3. **Select** `AI-powered-mental-wellness-platform`
4. **Add environment variable:**
   - `GEMINI_API_KEY` = `AIzaSyAna41mz8HodZH1bZ6B-okMEZKXkbEcciE`
5. **Deploy automatically**

---

## **Option 4: Render (Free)**

### **Steps:**
1. **Go to** [render.com](https://render.com)
2. **Connect GitHub** repository
3. **Create Web Service**
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
6. **Add environment variable**: `GEMINI_API_KEY`

---

## **Quick Deploy Commands**

### **For Streamlit Cloud:**
```bash
# Push latest changes
git add .
git commit -m "Deploy: Add Streamlit Cloud configuration"
git push origin main

# Then deploy via web interface
```

### **For Heroku:**
```bash
# Create Heroku files
echo "web: streamlit run streamlit_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
echo "python-3.11.0" > runtime.txt

# Deploy
heroku create mitramind-wellness
heroku config:set GEMINI_API_KEY=AIzaSyAna41mz8HodZH1bZ6B-okMEZKXkbEcciE
git push heroku main
```

---

## **Recommended: Streamlit Cloud**
- **Easiest setup** (5 minutes)
- **Free hosting**
- **Automatic updates** from GitHub
- **Built-in secrets management**
- **Custom domain** support

**Start here**: [share.streamlit.io](https://share.streamlit.io)