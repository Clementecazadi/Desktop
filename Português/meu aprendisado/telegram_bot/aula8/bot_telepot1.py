from pprint import pprint
import telepot
from telepot.loop import MessageLoop

TOKEN = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
bot = telepot.Bot(TOKEN)


def handle(msg):
    pprint(msg)


MessageLoop(bot, handle).run_as_thread()
