import random
from datetime import datetime


# -----------------------------
# Bot Functions
# -----------------------------

def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    return current_time


def get_date():
    current_date = datetime.now().strftime("%d %B %Y")
    return current_date


def get_day():
    current_day = datetime.now().strftime("%A")
    return current_day


def get_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning! 🌅"

    elif hour < 17:
        return "Good afternoon! ☀️"

    elif hour < 21:
        return "Good evening! 🌆"

    else:
        return "Good night! 🌙"


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "Why did the computer go to the doctor? Because it had a virus! 😂",
        "Why was the Python programmer confused? Because he couldn't find his indentation! 🐍",
        "Why did the programmer quit his job? Because he didn't get arrays! 😂"
    ]

    return random.choice(jokes)


def show_help():
    print("""
Bot: Here are the commands I understand:

hello       - Get a greeting
good morning - Morning greeting
good afternoon - Afternoon greeting
good evening - Evening greeting
good night  - Night greeting
name        - Ask my name
time        - Show current time
date        - Show today's date
day         - Show today's day
joke        - Tell a joke
help        - Show commands
bye         - Exit chatbot
""")


# -----------------------------
# Main Chatbot
# -----------------------------

def chatbot():

    print("=" * 45)
    print("             MINI CHATBOT 🤖")
    print("=" * 45)

    print("Bot: Hello! I'm MiniBot.")
    print("Bot:", get_greeting())
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' to exit.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        # -------------------------
        # General Greeting
        # -------------------------

        if user_input in ["hello", "hi", "hey"]:

            print("Bot:", get_greeting())

        # -------------------------
        # Morning
        # -------------------------

        elif user_input in ["good morning", "morning"]:

            print("Bot: Good morning! 🌅")
            print("Bot: I hope you have a great day!")

        # -------------------------
        # Afternoon
        # -------------------------

        elif user_input in ["good afternoon", "afternoon"]:

            print("Bot: Good afternoon! ☀️")
            print("Bot: How is your day going?")

        # -------------------------
        # Evening
        # -------------------------

        elif user_input in ["good evening", "evening"]:

            print("Bot: Good evening! 🌆")
            print("Bot: Hope you had a productive day!")

        # -------------------------
        # Night
        # -------------------------

        elif user_input in ["good night", "night"]:

            print("Bot: Good night! 🌙")
            print("Bot: Sleep well and take care! 😴")

        # -------------------------
        # Name
        # -------------------------

        elif user_input in [
            "name",
            "what is your name",
            "who are you"
        ]:

            print("Bot: My name is MiniBot.")
            print("Bot: I am a simple chatbot made with Python! 🤖")

        # -------------------------
        # Time
        # -------------------------

        elif user_input in [
            "time",
            "what is the time",
            "current time"
        ]:

            print("Bot: The current time is", get_time())

        # -------------------------
        # Date
        # -------------------------

        elif user_input in [
            "date",
            "today",
            "what is the date"
        ]:

            print("Bot: Today's date is", get_date())

        # -------------------------
        # Day
        # -------------------------

        elif user_input in [
            "day",
            "what day is today"
        ]:

            print("Bot: Today is", get_day())

        # -------------------------
        # Joke
        # -------------------------

        elif user_input in [
            "joke",
            "tell me a joke"
        ]:

            print("Bot:", tell_joke())

        # -------------------------
        # Help
        # -------------------------

        elif user_input in ["help", "commands"]:

            show_help()

        # -------------------------
        # Exit
        # -------------------------

        elif user_input in [
            "bye",
            "exit",
            "quit"
        ]:

            print("Bot: Goodbye! 👋")
            print("Bot: See you next time!")
            break

        # -------------------------
        # Unknown Command
        # -------------------------

        else:

            print("Bot: Sorry, I don't understand that yet. 😅")
            print("Bot: Type 'help' to see the available commands.")


# -----------------------------
# Start Chatbot
# -----------------------------

chatbot()