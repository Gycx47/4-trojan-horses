bot_name = "Hal"
print("You are now speaking to Hal, our health pal!")
print(f"{bot_name}: Hello! I'm {bot_name}, your health pal, how may I help you today?")

while True:
    user_input: str = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print(f"{bot_name}: Hello! How can I help?")

    elif user_input in ["bye", "see you", "goodbye"]:
        print(f"{bot_name}: Have a great day!")

    else:
        break

from google import genai

client = genai.Client(api_key=)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    print(f"\nHaL: {response.text}")