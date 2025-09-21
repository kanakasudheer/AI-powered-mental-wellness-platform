#!/usr/bin/env python3
"""
Quick launcher for MitraMind Streamlit app
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies. Please run: pip install -r requirements.txt")
        return False
    return True

def run_streamlit():
    """Launch Streamlit app"""
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
    except KeyboardInterrupt:
        print("\n🌱 MitraMind session ended. Take care!")
    except Exception as e:
        print(f"❌ Error running app: {e}")

if __name__ == "__main__":
    print("🌱 Starting MitraMind...")
    
    # Check if requirements are installed
    try:
        import streamlit
        import google.generativeai
        print("✅ Dependencies found!")
    except ImportError:
        print("📦 Installing dependencies...")
        if not install_requirements():
            sys.exit(1)
    
    print("🚀 Launching MitraMind chatbot...")
    run_streamlit()