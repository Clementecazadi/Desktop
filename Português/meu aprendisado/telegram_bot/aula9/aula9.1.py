import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
update = Updater(oTOKEN)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá eu sou o robo do telegram.")


start_handler = commandhandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.start_polling()
