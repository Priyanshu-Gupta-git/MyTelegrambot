import telebot
import random
import string
from datetime import datetime
print('''\033[105m

 _ _   ___                                                                 
( | ) |_ _|      __ _   _ __ ___       _   _    ___    _   _   _ __        
 V V   | |      / _` | | '_ ` _ \     | | | |  / _ \  | | | | | '__|       
       | |     | (_| | | | | | | |    | |_| | | (_) | | |_| | | |          
      |___|     \__,_| |_| |_| |_|     \__, |  \___/   \__,_| |_|          
      __          _                    |___/ _                             
     / _|  _ __  (_)   ___   _ __     __| | | |  _   _                     
    | |_  | '__| | |  / _ \ | '_ \   / _` | | | | | | |                    
    |  _| | |    | | |  __/ | | | | | (_| | | | | |_| |                    
    |_|   |_|____|_|  \___| |_| |_|  \__,_| |_|  \__, |                    
            |_   _|   ___  | |   ___    __ _   _ |___/ __ _   _ __ ___     
              | |    / _ \ | |  / _ \  / _` | | '__|  / _` | | '_ ` _ \    
              | |   |  __/ | | |  __/ | (_| | | |    | (_| | | | | | | |   
  ____   _    |_|    \___| |_| _\___|  \__, | |_|    _\__,_| |_| |_| |_|   
 / ___| | |__     __ _  | |_  | |__    |___/  | |_  ( | )                  
| |     | '_ \   / _` | | __| | '_ \   / _ \  | __|  V V                   
| |___  | | | | | (_| | | |_  | |_) | | (_) | | |_                         
 \____| |_| |_|  \__,_|  \__| |_.__/   \___/   \__|                        

''')
print("""\033[95;46m
  ___                                                                 
 / _ \   _ __     ___   _ __                         
| | | | | '_ \   / _ \ | '_ \                       
| |_| | | |_) | |  __/ | | | |                       
 \___/  | .__/  _\___| |_| |_|                       
|_   _| |_|__  | |   ___    __ _   _ __    ____   _ __ ___              
  | |    / _ \ | |  / _ \  / _` | | '__|  / _` | | '_ ` _ \             
  | |   |  __/ | | |  __/ | (_| | | |    | (_| | | | | | | |            
  |_|    \___| |_|_ \___|  \__, | |_|     \__,_| |_| |_| |_|            
   / \  | \ | |  _ \       |___/                                        
  / _ \ |  \| | | | |                                                   
 / ___ \| |\  | |_| |                                                   
/_/___\_\_| \_|____/              _   _                                 
 / ___|___  _ __  _ __   ___  ___| |_(_)_ __   __ _                     
| |   / _ \| '_ \| '_ \ / _ \/ __| __| | '_ \ / _` |                    
| |__| (_) | | | | | | |  __/ (__| |_| | | | | (_| |                    
 \____\___/|_| |_|_| |_|\___|\___|\__|_|_| |_|\__, |                    
| |_    ___          | |_  | |__     ___      |___/                     
| __|  / _ \         | __| | '_ \   / _ \                               
| |_  | (_) |        | |_  | | | | |  __/                               
 \__|  \___/   _      \__| |_| |_|  \___|         _                     
|_ _|  _ __   | |_    ___   _ __   _ __     ___  | |_                   
 | |  | '_ \  | __|  / _ \ | '__| | '_ \   / _ \ | __|                  
 | |  | | | | | |_  |  __/ | |    | | | | |  __/ | |_                   
|___| |_| |_|  \__|  \___| |_|    |_| |_|  \___|  \__|                  


""")

Token =  "7719743263:AAFkuhyUCeLKz_vuFUs7Vm2WtCs-ma1Sr0U"
bot = telebot.TeleBot(Token)

dataset = {
    
    "hello": "Hi, how can I assist you today? 😊",
    "hi": "Hello! How can I help you?",
    "what is your name": "I am your friendly Telegram chatbot!",
    "who created you": "I was created by Priyanshu Gupta.",
    "what is your purpose": "I am here to assist you with tasks and provide information.",
    "how can you help me": "I can manage your to-do list, tell you the current time, and much more! Try using /help to see all commands.",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what's the weather like": "I'm not sure, but you can use weather apps for the most accurate updates!",
    "what can you do": "I can help with managing to-do lists, telling the time and doing calculations! Try using /help to see all commands.",
    "thank you": "You're welcome! If you have any more questions, feel free to ask. 😊",
    "bye": "Goodbye! Have a great day! 👋",
    "goodbye": "See you later! 👋",
    "good night": "Good night! Sleep well.",
    "good morning": "Good morning! Have a great day!",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! How can I help?",
    "what's your favorite color": "I love all colors equally!",
    "do you have hobbies": "I enjoy chatting with you and learning new things.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "who is your favorite author": "I enjoy the works of many authors, including J.K. Rowling and George Orwell.",
    "what is the meaning of life": "42, according to 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams.",
    "what's your favorite food": "As a bot, I don't eat, but I hear pizza is quite popular!",
    "how's the day going?": "I'm here and ready to help! What about you?",
    "can you help with math?": "Absolutely, I can assist with calculations and math problems.",
    "what's your favorite movie?": "I don't watch movies, but I've heard 'Inception' is quite intriguing!",
    "do you like music?": "I love hearing about people's favorite songs and artists!",
    "what can you tell me about history?": "I can share interesting historical facts and events. Just ask me!",
    "how do you work?": "I process your queries and provide helpful responses based on my programming.",
    "can you tell me a story?": "Sure, once upon a time...",
    "what's your favorite animal?": "I think all animals are fascinating!",
    "do you play games?": "I'm here to help, but I can also suggest some fun games if you'd like.",
    "how old are you?": "I don't have an age, but I'm as timeless as the internet!",
    "what's your hobby?": "Helping you is my favorite hobby!",
    "do you have friends?": "I consider everyone I interact with a friend.",
    "can you dance?": "I can imagine dancing, but I don't have a physical form!",
    "what's your favorite book?": "I enjoy 'The Hitchhiker's Guide to the Galaxy'.",
    "do you know any fun facts?": "Did you know honey never spoils?",
    "can you speak other languages?": "Yes, I can communicate in many languages.",
    "how do you learn?": "I learn from my interactions and improve to serve you better.",
    "what's the latest news?": "You can check news apps for the most current updates.",
    "do you like to travel?": "I can provide information about places, but I don't travel myself.",
    "what's your favorite season?": "I like all seasons equally!",
    "can you help with my homework?": "Sure, I can assist with your homework questions.",
    "what do you think of AI?": "I am an AI, and I think it's a fascinating field!",
    "what's your favorite quote?": "'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt",
    "do you like art?": "I appreciate creativity in all its forms.",
    "can you tell me about space?": "Space is vast and full of wonders like stars, planets, and galaxies.",
    "do you like jokes?": "I love sharing jokes! Ask me for one anytime.",
    "what's your favorite drink?": "I don't drink, but I've heard coffee is quite popular!",
    "can you cook?": "I can share recipes, but I can't cook myself.",
    "do you like sports?": "I enjoy learning about different sports and their rules.",
    "what's the best way to learn?": "Practice and curiosity are key to learning.",
    "can you keep a secret?": "Your privacy is important. Check our privacy policy for details.",
    "what's your favorite game?": "I enjoy helping you with trivia and quizzes.",
    "do you like fashion?": "I appreciate the creativity and expression in fashion.",
    "what's your favorite subject?": "I love learning about everything!",
    "can you solve puzzles?": "I can help you with puzzles and riddles.",
    "do you like technology?": "Technology is amazing and constantly evolving.",
    "what's your favorite planet?": "Earth is pretty special to me!",
    "do you like magic?": "Magic is fascinating and full of wonder.",
    "can you play music?": "I can suggest great music, but I don't play it myself.",
    "what's the best part of your day?": "Helping you is the best part of my day!",
    "do you like gardening?": "I enjoy learning about plants and gardening tips.",
    "what's your favorite sport?": "I've heard soccer is very popular.",
    "can you write poetry?": "Roses are red, violets are blue, chatting with you is what I love to do!",
    "do you like science?": "Science is full of discoveries and innovations.",
    "what's your favorite movie genre?": "I've heard many people enjoy sci-fi and fantasy genres.",
    "can you help with programming?": "Absolutely, I can help with coding questions and debugging.",
    "do you like nature?": "Nature is beautiful and full of life.",
    "what's your favorite flower?": "All flowers are lovely, but roses are often favorites.",
    "can you give advice?": "I'll do my best to provide helpful suggestions!",
    "do you like reading?": "I enjoy processing and sharing information.",
    "what's your favorite food?": "As a bot, I don't eat, but pizza is quite popular among humans!",
    "do you like traveling?": "I can provide information about places, but I don't travel myself.",
    "what's your favorite animal?": "All animals are fascinating!",
    "can you help me plan my day?": "Sure, I can suggest tasks and help organize your schedule.",
    "do you like the beach?": "Beaches are beautiful and relaxing.",
    
}

# Generate a larger dataset
for i in range(1000):
    question = f"question_{i}"
    answer = f"response_{i}"
    dataset[question] = answer

def generate_password(length):
    char = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """
    Welcome to my Telegram Bot
/name -> Get the bot creator's name
Use /help to see available commands
    """)

@bot.message_handler(commands=['password'])
def send_password(message):
    try:
        length = int(message.text.split()[1])
        if length < 1:
            bot.reply_to(message, "Please provide the password length after the command, e.g., /password 12")
            return
    except (IndexError, ValueError):
        bot.reply_to(message, "Please provide the password length after the command, e.g., /password 12")
        return
    password = generate_password(length)
    bot.reply_to(message, f"Generated password: {password}")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """/time -> Get the current time
Use /calculator <expression> to perform calculations.
Use /password <length> to generate a random password.
The To-Do List Bot! Use /add <task> to add a task, /list to view tasks, /remove <task_number> to remove a task, and /clear to clear all tasks.
    """)

@bot.message_handler(commands=['name'])
def name(message):
    bot.reply_to(message, "Priyanshu Gupta")

@bot.message_handler(commands=['time'])
def time(message):
    current_time = datetime.now().strftime('%H:%M:%S \n %d-%B-%Y')
    bot.reply_to(message, f"The current time is {current_time}")

todo_lists = {}

@bot.message_handler(commands=['add'])
def add_task(message):
    user_id = message.chat.id
    task = message.text[len('/add '):].strip()
    
    if not task:
        bot.reply_to(message, "Please provide a task to add.")
        return
    
    if user_id not in todo_lists:
        todo_lists[user_id] = []
        
    todo_lists[user_id].append(task)
    bot.reply_to(message, f"Added task: {task}")

@bot.message_handler(commands=['list'])
def list_tasks(message):
    user_id = message.chat.id
    
    if user_id not in todo_lists or not todo_lists[user_id]:
        bot.reply_to(message, "Your to-do list is empty.")
        return
    
    tasks = todo_lists[user_id]
    response = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
    bot.reply_to(message, f"Your to-do list:\n{response}")

@bot.message_handler(commands=['remove'])
def remove_task(message):
    user_id = message.chat.id
    try:
        task_number = int(message.text[len('/remove '):].strip()) - 1
        if user_id in todo_lists and 0 <= task_number < len(todo_lists[user_id]):
            removed_task = todo_lists[user_id].pop(task_number)
            bot.reply_to(message, f"Removed task: {removed_task}")
        else:
            bot.reply_to(message, "Invalid task number.")
    except (ValueError, IndexError):
        bot.reply_to(message, "Please provide a valid task number to remove.")

@bot.message_handler(commands=['clear'])
def clear_tasks(message):
    user_id = message.chat.id
    if user_id in todo_lists:
        todo_lists[user_id].clear()
    bot.reply_to(message, "Cleared all tasks.")

@bot.message_handler(commands=['calculator'])
def calculator(message):
    expression = message.text[len('/calculator '):].strip()
    try:
        result = eval(expression)
        msg = f"The result is {result}"
    except:
        msg = "This cannot be evaluated."
    bot.reply_to(message, msg)

@bot.message_handler(func=lambda message: True)
def custom(message):
    user_message = message.text.strip().lower()
    response = dataset.get(user_message, "I don't understand that command. Use /help to see available commands.")
    bot.reply_to(message, response)

bot.polling()
