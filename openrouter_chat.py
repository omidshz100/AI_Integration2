#!/usr/bin/env python3
"""
OpenRouter AI Chat Script

A simple command-line chat application that connects to OpenRouter.ai API.

Dependencies:
- Install requests library: pip install requests

Usage:
1. Replace 'YOUR_OPENROUTER_API_KEY' with your actual OpenRouter API key
2. Run the script: python openrouter_chat.py
3. Type your messages and press Enter to chat
4. Type 'exit' or 'quit' to end the conversation
"""

import requests
import json
import sys
from dotenv import load_dotenv
import os

# Configuration
# API_KEY = "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"  # Replace this with your actual OpenRouter API key
# API_URL = "https://openrouter.ai/api/v1/chat/completions"
# MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"


# Configuration
load_dotenv(override=True)  # This will override existing environment variables
# load_dotenv()  # Load environment variables from .env file
API_KEY = os.environ.get("
")  # Get API key from environment variable, returns None if not found
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"

print(API_KEY)

def send_message_to_ai(message, conversation_history):
    """
    Send a message to the OpenRouter API and return the AI's response.
    
    Args:
        message (str): The user's message
        conversation_history (list): List of previous messages for context
    
    Returns:
        str: The AI's response, or None if there was an error
    """
    # Add the new user message to conversation history
    conversation_history.append({"role": "user", "content": message})
    
    # Prepare the request headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Prepare the request payload
    payload = {
        "model": MODEL,
        "messages": conversation_history,
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        # Make the API request
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()
            
            # Extract the AI's message
            ai_message = response_data['choices'][0]['message']['content']
            
            # Add AI response to conversation history
            conversation_history.append({"role": "assistant", "content": ai_message})
            
            return ai_message
        else:
            # Handle API errors
            print(f"Error: API request failed with status code {response.status_code}")
            try:
                error_data = response.json()
                print(f"Error details: {error_data.get('error', {}).get('message', 'Unknown error')}")
            except json.JSONDecodeError:
                print(f"Error response: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {str(e)}")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON response from API")
        return None
    except KeyError as e:
        print(f"Error: Unexpected response format - missing key {str(e)}")
        return None

def main():
    """
    Main chat loop that handles user input and AI responses.
    """
    # Check if API key is set
    if API_KEY == "YOUR_OPENROUTER_API_KEY":
        print("⚠️  Warning: Please replace 'YOUR_OPENROUTER_API_KEY' with your actual OpenRouter API key.")
        print("You can get your API key from: https://openrouter.ai/keys")
        print("\nEdit this script and replace the API_KEY variable with your key.")
        print("\nContinuing anyway (will likely fail)...\n")
    
    # Initialize conversation history
    conversation_history = []
    
    print("🤖 OpenRouter AI Chat")
    print(f"Model: {MODEL}")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 Goodbye!")
                break
            
            # Skip empty messages
            if not user_input:
                continue
            
            # Send message to AI and get response
            print("\n🤔 Thinking...")
            ai_response = send_message_to_ai(user_input, conversation_history)
            
            if ai_response:
                print(f"\nAI: {ai_response}\n")
            else:
                print("\n❌ Failed to get response from AI. Please try again.\n")
                # Remove the failed user message from history
                if conversation_history and conversation_history[-1]["role"] == "user":
                    conversation_history.pop()
        
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Chat ended. Goodbye!")
            break

if __name__ == "__main__":
    main()