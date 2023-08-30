from pprint import pprint
import telepot
from telepot.loop import MessageLoop

TOKEN =
bot = telepot.Bot(TOKEN)


def handle(msg):
    pprint(msg)


MessageLoop(bot, handle).run_as_thread()
