import datetime

# ─────────────────────────────────────────
#  General Knowledge Dictionary
# ─────────────────────────────────────────
gk_answers = {
    "what is the capital of india"        : " The capital of India is New Delhi!",
    "what is the capital of usa"          : " The capital of USA is Washington D.C.!",
    "what is the capital of france"       : " The capital of France is Paris!",
    "what is the capital of japan"        : " The capital of Japan is Tokyo!",
    "what is the capital of china"        : " The capital of China is Beijing!",
    "what is the capital of uk"           : " The capital of UK is London!",
    "what is the capital of australia"    : " The capital of Australia is Canberra!",
    "what is the capital of germany"      : " The capital of Germany is Berlin!",
    "what is the capital of russia"       : " The capital of Russia is Moscow!",
    "what is the capital of pakistan"     : " The capital of Pakistan is Islamabad!",
    "what is the capital of canada"       : " The capital of Canada is Ottawa!",
    "who is the president of usa"         : " The President of USA is Donald Trump (2025).",
    "who is the prime minister of india"  : " The Prime Minister of India is Narendra Modi.",
    "what is the largest planet"          : " The largest planet in our solar system is Jupiter!",
    "what is the smallest planet"         : " The smallest planet in our solar system is Mercury!",
    "how many planets are in solar system": " There are 8 planets in our solar system.",
    "what is the longest river"           : " The longest river in the world is the Nile!",
    "what is the largest country"         : " The largest country by area is Russia!",
    "what is the tallest mountain"        : " The tallest mountain in the world is Mount Everest!",
    "what is the national animal of india": " The national animal of India is the Tiger!",
    "what is the national bird of india"  : " The national bird of India is the Peacock!",
    "what is the currency of india"       : " The currency of India is the Indian Rupee (₹)!",
    "what is the currency of usa"         : " The currency of USA is the US Dollar ($)!",
    "what is the speed of light"          : " The speed of light is 3,00,000 km/s!",
    "who invented the telephone"          : " The telephone was invented by Alexander Graham Bell.",
    "who invented the computer"           : " The computer was invented by Charles Babbage.",
    "who invented electricity"            : " Electricity was discovered by Benjamin Franklin.",
    "what is the full form of ai"         : " AI stands for Artificial Intelligence!",
    "what is the full form of india"      : " INDIA: Independent Nation Declared In August!",
    "how many days in a year"             : " There are 365 days in a year (366 in a leap year).",
    "how many hours in a day"             : " There are 24 hours in a day.",
    "what is the chemical formula of water": " The chemical formula of water is H₂O!",
    "what is the boiling point of water"  : " The boiling point of water is 100°C!",
    "who is the father of nation india"   : " The Father of the Nation of India is Mahatma Gandhi.",
}

# ─────────────────────────────────────────
#  Helper Functions
# ─────────────────────────────────────────

def get_greeting():
    """Returns a greeting based on the current time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning! "
    elif 12 <= hour < 17:
        return "Good Afternoon! "
    elif 17 <= hour < 21:
        return "Good Evening! "
    else:
        return "Good Night! "


def get_current_time():
    """Returns the current system time."""
    now = datetime.datetime.now()
    return now.strftime(" Current time is: %I:%M:%S %p")


def get_today_date():
    """Returns today's date with the day name."""
    today = datetime.datetime.now()
    return today.strftime(" Today's date is: %d %B %Y, %A")


def check_gk(user_input):
    """Searches the GK dictionary for a matching answer."""
    for question, answer in gk_answers.items():
        if question in user_input:
            return answer
    return None


def get_response(user_input):
    """Analyzes user input and returns the appropriate response."""
    text = user_input.lower().strip()

    # --- Greetings ---
    if text in ["hi", "hello", "hey", "hii"]:
        return f"Hello!  {get_greeting()} How can I help you today?"

    # --- Name ---
    elif "your name" in text:
        return "My name is AI Chatbot! I am an artificial intelligence program."

    # --- How are you ---
    elif "how are you" in text:
        return " I am doing great, thank you for asking! How are you?"

    # --- Time ---
    elif "time" in text:
        return get_current_time()

    # --- Date ---
    elif "date" in text or "today" in text:
        return get_today_date()

    # --- Creator ---
    elif "who made you" in text or "who created you" in text:
        return " I was created by a Python developer! I am coded in Python."

    # --- What can you do ---
    elif "what can you do" in text:
        return (" Here is what I can do:\n"
                "  ✅ Chat with you\n"
                "  ✅ Tell you the current Date & Time\n"
                "  ✅ Answer General Knowledge questions\n"
                "  ✅ Greet you based on the time of day!")

    # --- Thanks ---
    elif "thank" in text:
        return " You're welcome! I'm always here to help."

    # --- Bye ---
    elif text in ["bye", "goodbye", "good bye", "see you"]:
        return " Good Bye! See you again! Take care. "

    # --- General Knowledge ---
    else:
        gk = check_gk(text)
        if gk:
            return gk
        else:
            return (" I'm sorry, I don't know the answer to that.\n"
                    " Tip: Try asking General Knowledge questions like:\n"
                    "   → 'What is the capital of India?'\n"
                    "   → 'Who invented the telephone?'\n"
                    "   → 'What is the speed of light?'")


# ─────────────────────────────────────────
#  Main Chatbot Loop
# ─────────────────────────────────────────

def run_chatbot():
    """Main loop that keeps the chatbot running."""
    print("=" * 52)
    print("            🤖  AI CHATBOT  🤖")
    print("=" * 52)
    print(" Hello! I am your personal AI Chatbot.")
    print("   Start chatting! (Type 'bye' to exit)")
    print("=" * 52)

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            # Handle empty input
            if not user_input:
                print("🤖 Bot: Please type something! ")
                continue

            response = get_response(user_input)
            print(f"🤖 Bot: {response}")

            # Exit condition
            if user_input.lower().strip() in ["bye", "goodbye", "good bye", "see you"]:
                print("\n" + "=" * 52)
                print("     Chat ended. See you next time! ")
                print("=" * 52)
                break

        except KeyboardInterrupt:
            print("\n\n🤖 Bot: Interrupted! Good Bye! ")
            break


# ─────────────────────────────────────────
#  Entry Point
# ─────────────────────────────────────────

if __name__ == "__main__":
    run_chatbot()
