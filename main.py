#!/usr/bin/env python3
"""
MitraMind - AI-Powered Mental Wellness Companion for Youth
A minimal implementation focusing on core mental health support features
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.components.chat_interface import ChatInterface

def main():
    """Main entry point for MitraMind application"""
    try:
        # Initialize and run the chat interface
        chat_app = ChatInterface()
        chat_app.run()
        
    except KeyboardInterrupt:
        print("\n\nMitraMind session ended. Take care of yourself!")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart MitraMind and try again.")

if __name__ == "__main__":
    main()