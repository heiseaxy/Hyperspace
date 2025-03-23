import requests
import time
import random

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# List of 150 unique questions
questions = [
    "What's the best way to learn programming?",
    "How does quantum computing work?",
    "What are some healthy breakfast ideas?",
    "Can you explain blockchain technology?",
    "What's the weather like on Mars?",
    "How do I improve my photography skills?",
    "What are the benefits of meditation?",
    "How does artificial intelligence work?",
    "What's the history of the internet?",
    "Can you suggest some good books to read?",
    "What’s the meaning of life?",
    "How do I make a perfect cup of coffee?",
    "What are the latest space discoveries?",
    "How can I stay motivated to exercise?",
    "What’s the future of electric cars?",
    "How do I start a small business?",
    "What are some fun weekend activities?",
    "Can you explain the theory of relativity?",
    "What’s the best way to learn a language?",
    "How does the stock market work?",
    "What’s the best way to save money?",
    "How do I plan a trip abroad?",
    "What are the effects of climate change?",
    "How does Wi-Fi actually work?",
    "What’s the history of video games?",
    "How can I improve my public speaking?",
    "What’s the science behind rainbows?",
    "How do I grow indoor plants successfully?",
    "What are the benefits of drinking water?",
    "How does cryptocurrency mining work?",
    "What’s the history of chocolate?",
    "How can I reduce stress in my life?",
    "What are some tips for better sleep?",
    "How do solar panels generate electricity?",
    "What’s the best way to cook steak?",
    "How does the human brain process memory?",
    "What are some must-visit places in Europe?",
    "How do I start investing in stocks?",
    "What’s the difference between viruses and bacteria?",
    "How can I make my home more eco-friendly?",
    "What’s the history of the Olympic Games?",
    "How do I train a dog effectively?",
    "What are the benefits of yoga?",
    "How does 3D printing work?",
    "What’s the best way to learn guitar?",
    "How do airplanes stay in the air?",
    "What are some creative writing tips?",
    "How does the immune system fight diseases?",
    "What’s the future of space travel?",
    "How can I improve my time management?",
    "What’s the history of pizza?",
    "How do I create a budget?",
    "What are the benefits of recycling?",
    "How does virtual reality work?",
    "What’s the best way to study for exams?",
    "How do I make homemade bread?",
    "What are the causes of global warming?",
    "How does GPS technology work?",
    "What’s the history of photography?",
    "How can I boost my creativity?",
    "What are some tips for healthy eating?",
    "How do self-driving cars function?",
    "What’s the best way to learn cooking?",
    "How does the moon affect tides?",
    "What are some fun science experiments?",
    "How do I start a podcast?",
    "What’s the history of democracy?",
    "How can I improve my drawing skills?",
    "What are the benefits of journaling?",
    "How does nuclear energy work?",
    "What’s the best way to plan a party?",
    "How do I maintain a car properly?",
    "What are some tips for traveling cheap?",
    "How does the internet of things work?",
    "What’s the history of coffee?",
    "How can I learn to code faster?",
    "What are the benefits of team sports?",
    "How do black holes form?",
    "What’s the best way to declutter my home?",
    "How does machine learning differ from AI?",
    "What are some tips for gardening?",
    "How do I make a good first impression?",
    "What’s the history of the English language?",
    "How can I stay productive working from home?",
    "What are the benefits of learning history?",
    "How does the human eye see color?",
    "What’s the best way to train for a marathon?",
    "How do I start a blog?",
    "What are some unusual animal facts?",
    "How does sound travel through the air?",
    "What’s the history of fashion?",
    "How can I improve my negotiation skills?",
    "What are the benefits of mindfulness?",
    "How do I build a simple website?",
    "What’s the best way to learn math?",
    "How does evolution work?",
    "What are some tips for reducing waste?",
    "How do I choose a good wine?",
    "What’s the future of renewable energy?",
    "What is the capital of France?",
    "What is the capital of France?",
	"Who wrote Romeo and Juliet?",
	"What is 7 × 8?",
    "Define artificial intelligence.",
	"What is the square root of 144?",
	"Who painted the Mona Lisa?",
	"What is the chemical symbol for gold?",
	"Translate ‘hello’ into Spanish.",
	"What year did the Titanic sink?",
	"Who discovered gravity?",
	"What is the boiling point of water in Celsius?",
	"What is the powerhouse of the cell?",
	"How many continents are there?",
	"Who was the first person to walk on the moon?",
	"What is the largest organ in the human body?",
	"What is the capital of Japan?",
	"How many bones are in the adult human body?",
	"Who wrote 1984?",
	"What is the first element on the periodic table?",
	"How many sides does a hexagon have?",
	"Who developed the theory of relativity?",
	"What is the speed of light in a vacuum?",
	"What is the longest river in the world?",
	"Which planet is known as the Red Planet?",
	"What is the currency of the United Kingdom?",
	"How many time zones are there in the world?",
	"Who invented the telephone?",
	"What is the largest mammal on Earth?",
	"What is the freezing point of water in Fahrenheit?",
	"What is the smallest prime number?",
	"Which element has the atomic number 6?",
	"What does DNA stand for?",
	"Who was the first president of the United States?",
	"How many chambers does the human heart have?",
	"What is the capital of Canada?",
	"What is the square of 15?",
	"What is the main gas in Earth’s atmosphere?",
	"Who wrote Pride and Prejudice?",
	"What is the process by which plants make their own food?",
	"How many legs does a spider have?",
	"What is the hardest naturally occurring mineral?",
	"Who was the Greek god of war?",
	"What is the SI unit of force?",
	"Which ocean is the largest?",
	"What is the longest bone in the human body?",
	"What is 9 cubed?",
	"What is the main ingredient in traditional Japanese miso soup?",
	"Who was the first woman to win a Nobel Prize?",
	"What is the main function of red blood cells?",
	"How many grams are in a kilogram?"
]

# Verify we have 100 questions
print(f"Total questions loaded: {len(questions)}")

# Function to send API request
def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Main bot loop
def run_chat_bot():
    print("Starting automated chat bot...")
    available_questions = questions.copy()  # Work with a copy to preserve original list
    
    for i in range(100):  # Fixed to 100 since we have exactly 100 questions
        if not available_questions:
            print("Ran out of questions unexpectedly!")
            break
        
        # Pick and remove a random question to avoid repetition
        question = random.choice(available_questions)
        available_questions.remove(question)
        
        # Send request and print results
        print(f"\nQuestion {i + 1}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        
        # Random delay between 1-10 seconds
        delay = random.uniform(1, 10)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)
    
    print("\nCompleted 150 questions!")

# Run the bot
if __name__ == "__main__":
    run_chat_bot()
