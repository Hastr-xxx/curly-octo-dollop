import logging

import keyboards as kb
from config import TOKEN

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, italic, code
from aiogram.types import ParseMode

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



fff = 'AgACAgIAAxkBAAICoGgpUfpIj4Bxv58crv31RwuKwz38AALU6DEbU8pQSf69zKKU-xPFAQADAgADcwADNgQ'
price_list = 'AgACAgIAAxkBAAICBWgpLquzHSxHsvm5hT6Y8bgei309AAK86DEbU8pQSerVycMUlQ_KAQADAgADcwADNgQ'
v1 = 'BAACAgIAAxkBAAICnGgpUTFcB-vJ6int6FyWcWhiA-UjAAJ5awACU8pQSYF1SjrMq_U1NgQ'
v2 = 'BAACAgIAAxkBAAICf2gpTxYhBdXxqzC72SoVcYUFkK5oAAJ1awACU8pQSYVxOipsW2_CNgQ'





@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Привет, {name}! Я Хастр, и здесь ты можешь сделать "
                        "заказ на арт у меня ✨"
                        "\n", reply_markup=kb.greet_kb)


@dp.message_handler(text=['Хочу сделать заказ!'])
async def process_command(message: types.Message):
    await message.answer("Выбери, что тебе нужно",
                        reply_markup=kb.inline_kb_full)



@dp.callback_query_handler(lambda call: True)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 3:
        await bot.answer_callback_query(callback_query.id)
        caption = 'Держи прайс-лист!\n'
        await bot.send_photo(callback_query.from_user.id, price_list, caption=caption,)
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text='Напиши свой заказ и пожелания к нему!\n'
                                                                 '\n(начни с "Заказ от @ссылканатвойтг")')



@dp.message_handler(text='btn3')
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, price_list,
                         reply_to_message_id=message.message_id)




help_message = text(
    "Доступные команды:\n",
    "/start - сделать заказ",
    "/prclst - прайс-лист",
    "/video1 - танец",
    "/video2 - собачки",
    "/photo - картинка",
    sep="\n"
)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)



@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, fff,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['prclst'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, price_list,
                         reply_to_message_id=message.message_id)



@dp.message_handler(commands=['video1'])
async def process_video_command(message: types.Message):
    await bot.send_video(message.from_user.id, v1,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['video2'])
async def process_video_command(message: types.Message):
    await bot.send_video(message.from_user.id, v2,
                         reply_to_message_id=message.message_id)




@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    m = msg.text
    if m[:5] == 'Заказ':
        message_text = text('Спасибо за заказ!\n'
                            'Скоро тебе напишут в лс для уточнения заказа')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
    else:
        message_text = text(('Хорошая попытка!'),
                            italic('\nНо просто напомню,'), 'что есть',
                            code('команда'), '/help')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)





if __name__ == '__main__':
    executor.start_polling(dp)