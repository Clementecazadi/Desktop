import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = 
update = Updater(oTOKEN)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá eu sou o robo do telegram.")


start_handler = commandhandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.start_polling()
