import requests
import random
import time

# 🔑 Input your API key here
API_KEY = "YOUR_API_KEY"

# 🌄 List of 100 diverse prompts
PROMPTS = [
    "A dreamy landscape with floating islands",
    "A dragon curled around a castle tower",
    "Futuristic robot bartender in a neon-lit bar",
    "A peaceful village under the stars",
    "Sunrise over the Grand Canyon",
    "An astronaut playing guitar on the moon",
    "A mystical forest glowing with bioluminescent plants",
    "Underwater city full of jellyfish and coral towers",
    "Steampunk airship flying through the clouds",
    "A cyberpunk street scene with glowing signs",
    # Add 90 more prompts below:
    "A majestic tiger in a jungle at dawn",
    "A pirate ship sailing through stormy seas",
    "A lonely cabin in a snowy mountain range",
    "A knight battling a fire-breathing dragon",
    "A futuristic battle between drones",
    "A fairytale castle on a cliffside",
    "A medieval market bustling with people",
    "Alien landscape with purple skies and two suns",
    "A zen garden with cherry blossom trees",
    "A wizard casting spells in a dark tower",
    "An enchanted book glowing on an ancient pedestal",
    "A crystal cave with glowing gems",
    "Post-apocalyptic city with overgrown nature",
    "A vintage steam train racing through mountains",
    "A magical portal opening in the forest",
    "A gladiator arena under a thunderstorm",
    "A UFO landing in a wheat field",
    "A colorful hot air balloon festival",
    "A neon jungle full of wild creatures",
    "A robot repairing a wind turbine",
    "Fantasy desert with giant bones and ruins",
    "A haunted house in a foggy field",
    "A sci-fi laboratory with AI experiments",
    "A mermaid under the sea near a treasure chest",
    "A lion resting in golden savanna light",
    "A fantasy king on his throne of flames",
    "A mountain with a giant face carved in it",
    "A spaceship flying past Saturn",
    "Viking warriors rowing through icy waters",
    "A cozy cottage during a thunderstorm",
    "A magical fox with glowing tails",
    "A child’s dreamscape of candy clouds",
    "A massive tree growing from a floating rock",
    "An owl flying through a midnight sky",
    "A fairy riding a hummingbird",
    "A wolf howling under the northern lights",
    "A street market on a rainy cyberpunk night",
    "A ballerina dancing on water",
    "A snowy owl perched on an icy branch",
    "A secret temple hidden in the jungle",
    "A turtle city moving across the desert",
    "A surreal clock tower melting in the sky",
    "A man walking into a digital portal",
    "A mushroom forest inhabited by tiny creatures",
    "A phoenix rising from the ashes",
    "A knight facing a giant golem",
    "A magical bridge made of light",
    "A floating palace above the clouds",
    "A peaceful lake reflecting twin moons",
    "A samurai in a field of falling cherry blossoms",
    "An enchanted violin playing itself",
    "A mirror dimension of a normal city",
    "A magician pulling stars from a hat",
    "A black cat walking across floating books",
    "A colorful nebula shaped like a butterfly",
    "A circus in the clouds",
    "A panda floating in space with balloons",
    "A desert temple glowing with ancient runes",
    "A fairy tale library guarded by dragons",
    "A knight riding a giant hummingbird",
    "A celestial whale swimming through stars",
    "A glowing sword embedded in stone",
    "A snow-covered village with magical lights",
    "A haunted carousel spinning in fog",
    "A galaxy formed from music notes",
    "A robot painting a sunset",
    "A jungle with ancient robot ruins",
    "A portal in the sky raining stars",
    "A forest fire tamed by magical deer",
    "A jellyfish spaceship orbiting Earth",
    "A neon-lit train running through space",
    "A child with wings flying over rooftops",
    "A volcanic island floating in the sky",
    "A deer with glowing antlers in the woods",
    "A steam-powered elephant walking through jungle",
    "A lunar base under construction",
    "A floating garden with colorful birds",
    "A battle between sky pirates",
    "A robot and dog under a streetlamp",
    "A fantasy town square during a festival",
    "A dragon made of clouds",
    "A castle inside a giant crystal",
    "A clockwork bird flying over rooftops",
    "A starry night over alien mountains",
    "A knight forging a sword in lava",
    "A futuristic samurai with plasma armor",
    "A cave of mirrors with infinite reflections",
    "A dragon egg hatching on a mountaintop",
    "A carousel flying through the sky",
    "A ship made of stars sailing the galaxy",
    "A frozen waterfall sparkling in the moonlight",
    "A wolf made of smoke and shadows",
    "A chessboard floating in the void",
    "A sunrise on a frozen alien world",
    "A pegasus flying above waterfalls"
]

# 📌 Function to send image generation request
def generate_image(prompt):
    url = "https://api.hyperbolic.xyz/v1/image/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model_name": "SDXL1.0-base",
        "prompt": prompt,
        "enable_refiner": "false",
        "negative_prompt": "",
        "strength": "0.8",
        "steps": "30",
        "cfg_scale": "5",
        "width": 1024,
        "height": 1024,
        "backend": "auto"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        print(f"✅ Prompt: \"{prompt}\"")
        print("🖼️  Result:", result)
    except requests.exceptions.HTTPError as err:
        print("❌ HTTP error:", err)
        print("Response:", response.text)
    except Exception as err:
        print("❌ Error:", err)

# 🧠 Main loop: shuffle and go through all prompts
def main():
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Please insert your API key at the top of the script.")
        return

    prompt_list = PROMPTS.copy()
    random.shuffle(prompt_list)

    print(f"🚀 Starting generation of {len(prompt_list)} prompts...\n")
    for idx, prompt in enumerate(prompt_list, 1):
        print(f"🔄 Generating image {idx}/{len(prompt_list)}...")
        generate_image(prompt)
        time.sleep(2)  # Optional delay to avoid overwhelming the server

    print("\n🎉 All prompts processed!")

if __name__ == "__main__":
    main()
