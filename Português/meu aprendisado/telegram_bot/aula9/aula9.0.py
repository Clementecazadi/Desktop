import asyncio
import telegram


async def main():
    TOKEN = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
    bot = telegram.Bot(TOKEN)
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())
