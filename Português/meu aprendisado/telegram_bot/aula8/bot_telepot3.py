import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep

TOKEN = 
bot = telepot.Bot(TOKEN)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Aperte', callback='Feito'),
         InlineKeyboardButton(text='Sim', callback='Ok'),
         InlineKeyboardButton(text='Não', callback='No')]
    ])
    bot.sendMessage(chat_id, 'Escolha uma opção abaixo:', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Apertou em' + str(query_data))


MessageLoop(bot, {'chat': on_chat_message,
                  'callback': on_callback_query}).run_as_thread()
print('listening...')
while True:
    sleep(2)
