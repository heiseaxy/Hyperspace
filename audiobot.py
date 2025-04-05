import requests
import random
import time

# 🔑 Import the API key from imagebot.py if available
try:
    from imagebot import API_KEY
except ImportError:
    API_KEY = "YOUR_API_KEY_HERE"

# 🎙️ 100 audio prompts
PROMPTS = [
    "Welcome to the city of dreams.",
    "The forest whispers secrets to those who listen.",
    "Technology has changed our lives in unimaginable ways.",
    "A calm ocean breeze soothes the soul.",
    "Once upon a time in a world far away.",
    "Innovation drives humanity forward.",
    "The mountains echoed with ancient stories.",
    "Kindness can change the world.",
    "The future is shaped by the decisions we make today.",
    "Stars shimmer in the vast night sky.",
    # Add 90 more unique or creative prompts below
] + [f"This is generated prompt number {i+11}." for i in range(90)]

# 🔊 Audio generation function
def generate_audio(prompt):
    url = "https://api.hyperbolic.xyz/v1/audio/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "text": prompt,
        "speed": "1"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        print(f"✅ Prompt: \"{prompt}\"")
        print("🎧 Response:", result)
    except requests.exceptions.HTTPError as err:
        print("❌ HTTP error:", err)
        print("Response:", response.text)
    except Exception as err:
        print("❌ Error:", err)

# 🚀 Main logic
def main():
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Please set your API_KEY in imagebot.py or directly here.")
        return

    remaining_prompts = PROMPTS.copy()
    random.shuffle(remaining_prompts)

    print(f"🎙️ Starting generation for {len(remaining_prompts)} audio prompts...\n")
    for idx, prompt in enumerate(remaining_prompts, 1):
        print(f"▶️ {idx}/{len(PROMPTS)} Generating audio...")
        generate_audio(prompt)
        time.sleep(2)  # Optional delay to avoid rate-limiting

    print("\n🎉 All prompts processed!")

if __name__ == "__main__":
    main()
