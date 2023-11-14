import telebot
import os
from loguru import logger
from src.constants import keybords


class Bot:
 
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(func=lambda m: True)(self.echo_all)        
    def run(self):
        logger.info('runing ...')
        self.bot.infinity_polling()
        
    def echo_all(self,message):
        self.bot.send_message(message.chat.id, message.text, reply_markup=keybords.main)
        
                
                
                
if __name__ == '__main__':
    bot = Bot()
    bot.run()