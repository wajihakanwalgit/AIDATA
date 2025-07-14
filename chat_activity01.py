import re , random
from colorama import Fore, init
init(autoreset=True)
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],

    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts."
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def provide_recommendations(user_input):
    normalized_input = normalize_input(user_input)
    recommendations = []

    for category, places in destinations.items():
        if normalized_input in category:
            recommendations.extend(places)

    if not recommendations:
        recommendations = random.sample([place for sublist in destinations.values() for place in sublist], 3)

    print(Fore.CYAN + "Here are some recommendations for you:")
    for place in recommendations:
        print(Fore.GREEN + f"- {place}")
def offer_packing_tips(destination, duration):
    tips = {
        "beaches": "Don't forget your sunscreen, swimsuit, and a good book!",
        "mountains": "Pack warm clothes, sturdy boots, and a camera for the views!",
        "cities": "Comfortable shoes are a must, along with a portable charger!"
    }
    print(Fore.YELLOW + f"Packing tips for {destination} for {duration} days:")
    print(Fore.BLUE + tips.get(destination, "General packing tips: Bring essentials and stay hydrated!"))

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.MAGENTA + "Here's a joke for you:")
    print(Fore.RED + joke)
def display_help():
    print(Fore.YELLOW + "Help Menu:")
    print(Fore.CYAN + "1. Type 'recommend' followed by a category (beaches, mountains, cities) to get travel recommendations.")
    print(Fore.CYAN + "2. Type 'pack' followed by your destination and duration to get packing tips.")
    print(Fore.CYAN + "3. Type 'joke' to hear a random joke.")
    print(Fore.CYAN + "4. Type 'help' to see this menu again.")
    print(Fore.CYAN + "5. Type 'exit' to quit the chatbot.")
def chat():
    print(Fore.GREEN + "Welcome to the Travel Chatbot!")
    display_help()

    while True:
        user_input = input(Fore.YELLOW + "You: ")
        if user_input.lower() == "exit":
            print(Fore.RED + "Goodbye!")
            break
        elif user_input.lower().startswith("recommend"):
            category = user_input.split(" ", 1)[1]
            provide_recommendations(category)
        elif user_input.lower().startswith("pack"):
            _, destination, duration = user_input.split(" ", 2)
            offer_packing_tips(destination, duration)
        elif user_input.lower() == "joke":
            tell_joke()
        elif user_input.lower() == "help":
            display_help()
        else:
            print(Fore.RED + "Sorry, I didn't understand that.")
            display_help()
# Run the chatbot
if __name__ == "__main__":
    chat()