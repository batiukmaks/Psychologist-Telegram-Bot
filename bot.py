# Telegram bot for CS50x final project
# Bot gives you a range of available psychologists.
# When you choose it, psychologist responds to your message with his sound
# To use a bot for your own, you have to get a TOKEN and write it in 'config.py' file

# Inspired by 'Rubber duck debugging' method and CS50's IDE's 'DUCK DEBUGGER' chat

import telebot
import config
import random
import os
import time

bot = telebot.TeleBot(config.TOKEN)

# Information about our psychologists
psychologistsBio = [
    {'name': 'Mr Dog', 'id': 1, 'description': 'Name: Mr Dog 🐶 \n37 years old \nWorks for 15 years \nLoves you more than himself 💛',
        'imageDirectory': 'static/mr_dog.jpg', 'sound': 'bark'},
    {'name': 'Mr Duck', 'id': 2, 'description': 'Name: Mr Duck 🦆 \n56 years old \nWorks for 23 years \nThat one, who has inspired me to create this center 💡',
        'imageDirectory': 'static/mr_duck.png', 'sound': 'quack'},
    {'name': 'Mr Hamster', 'id': 3, 'description': 'Name: Mr Hamster 🐹 \n23 years old \nWorks for 1 year \nDoes not have much experience, but he can lie down on your hands and you will never be unhappy again 💚',
        'imageDirectory': 'static/mr_hamster.jpg', 'sound': 'squeak'},
    {'name': 'Mrs Kitty', 'id': 4, 'description': 'Name: Mrs Kitty aka Pretty-Kitty 🐱 \n27 years old \nWorks for 5 years \nThat is a cat. Not a word more ❤️',
        'imageDirectory': 'static/mrs_kitty.png', 'sound': 'meow'}
]

# Psychologists' names (will use to make a menu)
psychologistsNames = []
for person in psychologistsBio:
    psychologistsNames.append(person['name'])

# Psychologist, chosen by user
chosenSpecialist = 0

# Greeting and instruction after starting the session


@bot.message_handler(commands="start")
def greeting(message):
    global chosenSpecialist
    chosenSpecialist = 0
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    psychologists = telebot.types.KeyboardButton('Available psychologists')
    markup.add(psychologists)

    bot.send_message(message.chat.id, "Hello! \nThis is a psychology center where you can get help. \nChoose the specialist to talk by pressing a button 'Available psychologists'", reply_markup=markup)

# Ending the session. Delete chosen psychologists


@bot.message_handler(commands='end')
def end(message):
    global chosenSpecialist
    chosenSpecialist = 0
    bot.send_message(
        message.chat.id, "The session is ended! \nHope you are feeling better now. \n\nTo start a new session enter /start")

# Send psychologists' photos and descriptions


def send_list_of_psychologists(message):
    for person in psychologistsBio:
        time.sleep(1)
        image = open(person["imageDirectory"], 'rb')
        bot.send_photo(message.chat.id, image)
        bot.send_message(
            message.chat.id, person["description"], reply_markup=sendChoosingMenu())

# Send a menu (to choose a psychologist)


def sendChoosingMenu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for person in psychologistsBio:
        item = telebot.types.KeyboardButton(person['name'])
        markup.add(item)
    return markup

# Work with text and menu


@bot.message_handler(content_types=["text"])
def menu(message):
    if message.chat.type == 'private':
        input = message.text
        global chosenSpecialist

        # Send a menu to choose a psychologist
        if input == 'Available psychologists':
            send_list_of_psychologists(message)
            sendChoosingMenu()
            bot.send_message(
                message.chat.id, "Choose your specialist!", reply_markup=sendChoosingMenu())

        # Check if user chose a psychologist
        elif input in psychologistsNames and chosenSpecialist == 0:
            # Find chosen psychologist
            for psychologist in psychologistsBio:
                if input == psychologist['name']:
                    # Remember chosen psychologist
                    chosenSpecialist = psychologist['name']
                    # Remove created menu (for choosing a psychologist)
                    markup = telebot.types.ReplyKeyboardRemove()
                    bot.send_message(
                        message.chat.id, f"Good, you chose {psychologist['name']}. \nNow you can tell your story/problem and {psychologist['name']} will help you!", reply_markup=markup)
                    break

        # Actual work with psychologist
        else:
            # If user haven't chosen a psychologist
            if chosenSpecialist == 0:
                bot.send_message(
                    message.chat.id, "You have not chosen specialist!")
            # Else send psychologist's sound random times (from 1 to 3)
            else:
                times = random.randrange(1, 4)
                bot.send_message(message.chat.id, (psychologistsBio[psychologistsNames.index(
                    chosenSpecialist)]['sound'] + " ") * times)


# Helps our bot not to stop
if __name__ == '__main__':
    bot.infinity_polling()
