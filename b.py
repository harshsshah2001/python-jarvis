import time
import random
from datetime import datetime


# =========================================================
# AUTO REPLY CONFIGURATION
# =========================================================

BOT_NAME = "Python Auto Reply Bot"


# =========================================================
# REPLY DATABASE
# =========================================================

replies = {
    "hello": [
        "Hello! 👋 How can I help you?",
        "Hi! Nice to hear from you.",
        "Hey! How are you?"
    ],

    "hi": [
        "Hi! 👋",
        "Hello! How can I help you?",
        "Hey there!"
    ],

    "hey": [
        "Hey! 👋 How can I help you?",
        "Hello!",
        "Hey! What's up?"
    ],

    "good morning": [
        "Good morning! ☀️ Have a great day!",
        "Good morning! How can I help you?"
    ],

    "good afternoon": [
        "Good afternoon! 😊",
        "Good afternoon! How can I help you?"
    ],

    "good evening": [
        "Good evening! 🌙",
        "Good evening! How can I help you?"
    ],

    "how are you": [
        "I'm doing great! 😊 How are you?",
        "I'm fine, thank you! How can I help you?"
    ],

    "thank you": [
        "You're welcome! 😊",
        "No problem!",
        "My pleasure!"
    ],

    "thanks": [
        "You're welcome! 😊",
        "No problem!",
        "Anytime!"
    ],

    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ],

    "price": [
        "Sure! Please tell me which product you're interested in."
    ],

    "product": [
        "Sure! Please tell me the product name and I'll help you."
    ],

    "contact": [
        "Sure! Please share your requirement and our team will contact you."
    ],

    "help": [
        "Sure! I'm here to help. Please tell me your requirement."
    ]
}


# =========================================================
# DEFAULT REPLY
# =========================================================

default_replies = [
    "Thanks for your message. We will get back to you shortly.",
    "Thank you for contacting us. How can we help you?",
    "We received your message. Please share more details.",
    "Thanks for reaching out! Our team will assist you soon."
]


# =========================================================
# FUNCTION: FIND REPLY
# =========================================================

def get_reply(message):

    # Convert message to lowercase
    message = message.lower().strip()

    # Check every keyword
    for keyword in replies:

        if keyword in message:

            # Select random reply
            return random.choice(replies[keyword])

    # If no keyword is found
    return random.choice(default_replies)


# =========================================================
# FUNCTION: SAVE CHAT
# =========================================================

def save_chat(user_message, bot_reply):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("chat_history.txt", "a", encoding="utf-8") as file:

        file.write(
            f"[{current_time}]\n"
            f"User: {user_message}\n"
            f"Bot: {bot_reply}\n"
            f"{'-' * 50}\n"
        )


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    print("=" * 50)
    print(f"       {BOT_NAME}")
    print("=" * 50)

    print("Bot is now running...")
    print("Type 'exit' to stop the bot.")
    print()

    while True:

        # Receive message
        user_message = input("You: ")

        # Stop bot
        if user_message.lower().strip() == "exit":

            print("Bot: Goodbye! 👋")
            break

        # Generate reply
        bot_reply = get_reply(user_message)

        # Show reply
        print("Bot:", bot_reply)

        # Save conversation
        save_chat(user_message, bot_reply)

        # Small delay to make it feel natural
        time.sleep(1)


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    main()