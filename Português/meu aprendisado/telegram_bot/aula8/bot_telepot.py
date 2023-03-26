from pprint import pprint
import telepot

TOKEN = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
bot = telepot.Bot(TOKEN)
pprint(bot.getUpdates())
bot.sendMessage(1422970424, "Ola meu clemente")
