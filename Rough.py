import telebot
import time
from data import token
import random

bot = telebot.TeleBot(token, parse_mode=None)
players = [1]
chat_id_list = []
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
global chat_id


@bot.message_handler(commands=['start', 'join'])
def player_join(message):                              # People press join to add in the players list
    global chat_id
    chat_id = message.chat.id
    user_id = message.from_user.id
    print("join is pressed")
    if message.text.startswith('/start'):
        if user_id not in players:
            players.append(user_id)
    elif message.text.startswith('/join'):
        if user_id not in players:
            players.append(user_id)
    print(players)

    #
    # @bot.message_handler(func=lambda message: message.text.startswith(str(int(a * b))))
    # def answer(message):
    #     if chat_id == message.chat.id:
    #         return True
    #     else:
    #         return False

    for i in players:
        a = random.choice(players)
        b = random.choice(players)
        bot.send_message(chat_id, f"{players[i]} your turn. \n {a} x {b} = ?")
        c = answer()
        d = str(a * b)

        @bot.message_handler(func=lambda message: message.text.startswith(d))
        def answer(message):
            if chat_id == message.chat.id:
                return True
            else:
                return False

        if c:
            bot.send_message(chat_id, f"Correct Answer @{players[i]}")
        else:
            bot.send_message(chat_id, "Wrong answer, You're Eliminated")
            players.remove(players[i])

        if len(players) == 1:
            bot.send_message(chat_id, f"{players[0]} is the Winner")
            break


bot.polling()

# while True:
#     c = random.choice(list1)
#     b = random.choice(list1)
#     bot.send_message(chat_id,f"{players[0]}, it's your turn.")
#     bot.send_message(f"\nMultiply {c} x {b}")
#     t = c * b
#     d = answer()
#     if d:
#         bot.send_message(chat_id, "\nCheers!\n")
#     else:
#         bot.send_message(chat_id, f"{players[0]}, You're eliminated. Correct answer is {t}\n."
#         )
#         players.remove(players[y])
#         y = 0
#
#     if len(players) == 1:
#         bot.send_message(chat_id,f" {players[y]} is the Winner. ")
#         break
#     y += 1
#     if len(players) == y:
#         y = 0
