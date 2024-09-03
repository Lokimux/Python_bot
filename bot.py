import telebot  # Import the Telebot library to interact with the Telegram API
import re  # Import the regular expressions module for string manipulation

# Step 1: Define the bot token from BotFather
bot = telebot.TeleBot("7380129005:AAFBdIDNPuXzVqQEqR47tE8v1jIn7L8CDxE")

# Step 2: Define a dictionary with responses for various Python concepts.
responses = {
    "print": "The `print()` function is used to display output to the console. Example: `print('Hello, World!')`.",
    "variable": "In Python, a variable is a container for storing data values. Example: `x = 10`.",
    "loop": "Loops in Python, like `for` and `while`, allow you to repeat code. Example: `for i in range(5): print(i)`.",
    "function": "A function is a block of reusable code that performs a specific task. Example: `def greet(): print('Hello')`.",
    "list": "A list is a collection of items in a particular order. Example: `my_list = [1, 2, 3]`.",
    "dictionary": "A dictionary stores data in key-value pairs. Example: `my_dict = {'name': 'John', 'age': 25}`.",
    "tuple": "A tuple is like a list, but it's immutable (cannot be changed). Example: `my_tuple = (1, 2, 3)`.",
    "set": "A set is an unordered collection of unique items. Example: `my_set = {1, 2, 3}`.",
    "class": "A class is a blueprint for creating objects (instances). Example: `class Dog: def __init__(self, name): self.name = name`.",
    "inheritance": "Inheritance allows a class to inherit attributes and methods from another class. Example: `class Puppy(Dog): pass`.",
}

# Step 3: Preprocess the user's input.
def preprocess_text(text):
    """
    Preprocess the user input by converting it to lowercase and removing punctuation.
    This step ensures that the bot can match keywords regardless of case or punctuation.
    """
    text = text.lower()  # Convert text to lowercase to make the bot case-insensitive
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation to focus on the words
    return text

# Step 4: Define a function to match the user's input with the appropriate response.
def get_response(user_input):
    """
    Return an appropriate response based on the user's input.
    The function checks if any predefined keyword is present in the input.
    If a match is found, it returns the corresponding response from the dictionary.
    """
    user_input = preprocess_text(user_input)  # Preprocess the user's input for easier matching

    # Check if any keyword in the dictionary matches the user's input
    for key in responses.keys():
        if key in user_input:  # If a keyword is found in the input
            return responses[key]  # Return the corresponding response
    
    # If no keyword matches, provide a default response
    return "I'm sorry, I don't understand that. Can you ask something else about Python?"

# Step 5: Handle the /start command.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Handle the /start command.
    When the user sends the /start command, this function will be triggered.
    The bot will greet the user and provide a brief introduction.
    """
    welcome_message = (
        "Hello! I'm your Python learning bot. 🤖\n"
        "Ask me anything about Python, and I'll do my best to help!\n\n"
        "For example, you can ask about `print`, `variables`, `loops`, `functions`, and more.\n"
        "Let's start learning!"
    )
    bot.reply_to(message, welcome_message)  # Send the welcome message to the user

# Step 6: Define the bot's response to general messages.
@bot.message_handler(func=lambda message: True)  # This handler responds to all messages
def send_response(message):
    """
    Respond to the user's message with the appropriate Python concept explanation.
    The bot processes the incoming message, checks for keywords, and replies with the relevant information.
    """
    user_input = message.text  # Get the text input from the user
    response = get_response(user_input)  # Get the chatbot's response based on the input
    bot.reply_to(message, response)  # Send the response back to the user on Telegram

# Step 7: Start polling for messages.
bot.polling()  # This starts the bot and keeps it running to listen for incoming messages
