import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv
from db import Session, User,Message
load_dotenv('.env')
# Bot token can be obtained via https://t.me/BotFather

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_telegram_id = str(message.from_user.id)
    username = message.from_user.username
    created = str(message.date)
    user = User(user_telegram_id=user_telegram_id,username=username,created=created)
    session = Session()
    session.add(user)
    session.commit()
    await message.reply("Ma`lumot saqlandi")
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message()
async def messages_from_users_handler(message: types.Message):
    text = str(message.text)
    created = str(message.date)
    Mess = Message(text=text,created=created)
    session = Session()
    session.add(Mess)
    session.commit()
    await message.reply("Habar saqlandi")

@dp.message()
async def echo_handler(message: types.Message) -> None:

    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(os.getenv('BOT_TOKEN'), parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
