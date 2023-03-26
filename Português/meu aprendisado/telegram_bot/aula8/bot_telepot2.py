import telepot
from telepot.loop import MessageLoop
from time import sleep

TOKEN = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
bot = telepot.Bot(TOKEN)


def handle(msg):
    # Glance devolve o tipo da mensagem pode ser texto, audio...
    # o tipo do chat pode ser privado o público,
    # e nos dá o chat ID para podermos responder.
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'] + '-- este é o texto repetido.')
    elif content_type == 'audio':
        pass


MessageLoop(bot, handle).run_as_thread()
print('Listening...')

# Keep the program running
while True:
    sleep(2)
