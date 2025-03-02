import urllib.request
import json
import os

# Get API key from environment variable (Set this in Render or GitHub secrets)
API_KEY = os.getenv("AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")

# Gemini API URL
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

# Function to generate AI response
def generate_code(prompt):
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    json_data = json.dumps(data).encode("utf-8")
    
    req = urllib.request.Request(API_URL, data=json_data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {str(e)}"

# If run directly, ask for user input
if __name__ == "__main__":
    prompt = input("Enter your coding prompt: ")
    print("\nGenerated Code:\n")
    print(generate_code(prompt))
