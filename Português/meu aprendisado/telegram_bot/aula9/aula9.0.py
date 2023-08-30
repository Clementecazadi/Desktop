import asyncio
import telegram


async def main():
    TOKEN =
    bot = telegram.Bot(TOKEN)
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())
