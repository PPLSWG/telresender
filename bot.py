# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Hello! \n\n Send me your track(s) for Pro Mastering. Write /help for full information.')

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'This bot is designed to receive your songs for professional mastering. Send your tracks in .WAV format [24 bit, 44100] The term of order execution is 1-3 days. We will send the finished result (maybe even several versions) directly to your account.')







@bot.message_handler(content_types=["text"])
def messages(message):
	if int(message.chat.id) == int(config.owner):
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
		bot.send_message(message.chat.id, '%s, wait please 👍'%message.chat.username)

if __name__ == '__main__':
	bot.polling(none_stop = True)
