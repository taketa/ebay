# -*- coding: utf-8 -*-
#!bot/bin/python
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	send = message.text.split(" ")
	print(len(send))
	if len(send)>1:
		bot.send_message(message.chat.id, "http://thumbs3.ebaystatic.com/m/mSFfuNZ807Bv-r5EXc4UfJw/140.jpg")

if __name__ == '__main__':
     bot.polling(none_stop=True)