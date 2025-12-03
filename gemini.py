bot_name = "Hal"
print("You are now speaking to Hal, our health pal!")
print(f"{bot_name}: Hello! I'm {bot_name}, your health pal, how may I help you today?")

import os
from google import genai

GEMINI_API_KEY = "AIzaSyDwMgiOf2WDzDoVNLkeP7dGDwHY8S5iKrc"
client = genai.Client(api_key=GEMINI_API_KEY)

prompt = f"""
    You are a helpful nutrition assistant. You must only use information from reliable, credible and verifiable sources, such as USDA FoodData Central database, Australia Food Composition Database or reputable nutrition journals and articles. 
    Do not use unrealiable websites, forums or general internet searches. Cite your sources. If there are no reliable information to be found, say "I'm sorry but I am unable to find any reliable nutrition information for that." 
    """
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=user_input
    )
    print(f"\nHaL: {response.text}")
