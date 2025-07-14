import colorama
from colorama import Fore, Style
from textblob import TextBlob
import sys
colorama.init(autoreset=True)
print(Fore.GREEN + Style.BRIGHT + "Text Analysis Tool")
usr_name = input(Fore.YELLOW + "Enter your name: ")
print(Fore.CYAN + f"Hello, {usr_name}! Let's analyze some text.")
if not usr_name:
    usr_name = "User_agent"
conversation_history = []

print(Fore.MAGENTA + "hello " + usr_name + "! I am your text analysis assistant.")
print(Fore.BLUE + "Please enter a sentence for analysis:")
print(f"type {Fore.BLUE} 'reset' {Fore.CYAN} ,{Fore.YELLOW} 'history' {Fore.CYAN} or {Fore.RED} 'exit' {Fore.CYAN} to quit{Style.RESET_ALL}\n"
      )
while True:
    user_input = input(Fore.YELLOW + "You: ")
    if user_input.lower() == 'exit':
        print(Fore.RED + "Exiting the program. Goodbye!")
        sys.exit()
    elif user_input.lower() == 'reset':
        conversation_history.clear()
        print(Fore.CYAN + "Conversation history has been reset.")
    elif user_input.lower() == 'history':
        print(Fore.MAGENTA + "Conversation History:")
        for i, sentence in enumerate(conversation_history, 1):
            print(f"{i}. {sentence}")
        continue
    else:
        print(Fore.GREEN + "Analyzing your input...")
        for idx ,(sentence) in enumerate(conversation_history, 1):
            if TextBlob(sentence).sentiment.polarity > 0:
                print(Fore.GREEN + f"{idx}. {sentence} - Positive sentiment detected.")
            elif TextBlob(sentence).sentiment.polarity < 0:
                print(Fore.RED + f"{idx}. {sentence} - Negative sentiment detected.")
            else:
                print(Fore.YELLOW + f"{idx}. {sentence} - Neutral sentiment detected.")
            continue
        polarity = TextBlob(user_input).sentiment.polarity
        if polarity > 0:
            print(Fore.GREEN + "Your input has a positive sentiment!")
            sentiment = "positive"
            color= Fore.GREEN
            emoji = "😊"
        elif polarity < 0:
            sentiment = "negative"
            color = Fore.RED
            emoji = "😞"
        else:
            sentiment = "neutral"
            color = Fore.YELLOW
            emoji = "😐"
        print(f"{color}Your input is {sentiment} {emoji}")

        conversation_history.append((user_input, polarity, sentiment))          
        print(Fore.CYAN + f"Your input has been added to the conversation history.")