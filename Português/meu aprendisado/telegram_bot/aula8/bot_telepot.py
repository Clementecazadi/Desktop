from pprint import pprint
import telepot

TOKEN = 
bot = telepot.Bot(TOKEN)
pprint(bot.getUpdates())
bot.sendMessage(1422970424, "Ola meu clemente")
