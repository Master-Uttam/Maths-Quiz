import telebot
import random
import time
from data import token

x = 0
"""
This is a math bot to challenge you math skills
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2 = [1]
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'join'])
def init_game(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print("Game is started")
    while time.sleep(10):
        if message.text.startswith('/start'):
            if user_id not in list2:
                list2.append(user_id)
        elif message.text.startswith('/join'):
            if user_id not in list2:
                list2.append(user_id)

    print(*list2)
    if len(list2) > 1:
        while True:
            for i in len(list2):
                if len(list2) != 1:
                    bot.send_message(chat_id, list2[i])
                    bot.send_message(chat_id, f"{list2[i]} it is your turn.\n "
                                              f"{random.choice(list1)}x{random.choice(list1)}=? \n")

                elif len(list2) == 1:
                    print(f"The Winner is {list2[0]}")
                    break

    else:
        print()


bot.polling()
