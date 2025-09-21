#!/usr/bin/env python3
"""
Test Gemini API integration
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.services.gemini_service import GeminiService

def test_gemini():
    print("Testing Gemini API integration...")
    
    try:
        gemini = GeminiService()
        
        # Test basic response
        test_message = "I'm feeling anxious about my exams"
        response = gemini.get_response(test_message)
        
        print(f"User: {test_message}")
        print(f"MitraMind: {response}")
        print("\nGemini API integration successful!")
        
    except Exception as e:
        print(f"Error testing Gemini API: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_gemini()