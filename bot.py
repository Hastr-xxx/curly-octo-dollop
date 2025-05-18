# Импортируем необходимые классы.
import keyboards as kb
from config import TOKEN

import logging
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, italic, code
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Сохраняем айди файлов
fff = 'AgACAgIAAxkBAAICoGgpUfpIj4Bxv58crv31RwuKwz38AALU6DEbU8pQSf69zKKU-xPFAQADAgADcwADNgQ'
price_list = 'AgACAgIAAxkBAAICBWgpLquzHSxHsvm5hT6Y8bgei309AAK86DEbU8pQSerVycMUlQ_KAQADAgADcwADNgQ'
v1 = 'BAACAgIAAxkBAAICnGgpUTFcB-vJ6int6FyWcWhiA-UjAAJ5awACU8pQSYF1SjrMq_U1NgQ'
v2 = 'BAACAgIAAxkBAAICf2gpTxYhBdXxqzC72SoVcYUFkK5oAAJ1awACU8pQSYVxOipsW2_CNgQ'
scetch1 = 'AgACAgIAAxkBAAIDH2gqE8saW2MndIP79Y2CAAHJjv3oGQACpfkxGy7gUEl4JN2nkvyzhwEAAwIAA3MAAzYE'
scetch2 = 'AgACAgIAAxkBAAIDIGgqE-6nWZtQO-CKI9sBubZVeYtrAAKn-TEbLuBQSdlyFe7U8auYAQADAgADcwADNgQ'
scetch3 = 'AgACAgIAAxkBAAIDIWgqFA59W8G2vgKi9KSyMs-NF4hHAAKp-TEbLuBQSbCd1OeY_EvIAQADAgADcwADNgQ'


# Создаем хэндлер команды start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Привет, {name}! Я Хастр, и здесь ты можешь сделать "
                        "заказ на арт у меня ✨"
                        "\n", reply_markup=kb.greet_kb)


# Создаем хэндлер с триггером в виде текста
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
        inline_kb_full2 = InlineKeyboardMarkup(row_width=1)
        inline_btn_4 = InlineKeyboardButton('Обратная связь',
                                            url='https://t.me/hastr_xxx')
        inline_kb_full2.add(kb.inline_btn_2, kb.inline_btn_5, inline_btn_4)
        await bot.send_photo(callback_query.from_user.id, price_list,
                             caption=caption,
                             reply_markup=inline_kb_full2)
    elif code == 4:
        inline_kb_full3 = InlineKeyboardMarkup(row_width=1)
        inline_btn_6 = InlineKeyboardButton('Скетчи', callback_data='btn6')
        inline_btn_7 = InlineKeyboardButton('Полноценные работы', callback_data='btn7')
        inline_kb_full3.add(inline_btn_6, inline_btn_7)

        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Выбери, что тебе нужно',
                               reply_markup=inline_kb_full3)
    elif code == 2:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               text='Напиши свой заказ и пожелания к нему!\n'
                                    '\n(начни с "Заказ от @ссылканатвойтг")')
    elif code == 6:
        caption = 'Скидка 50% от стоимости на любой скетч'
        await bot.send_photo(callback_query.from_user.id, scetch2,
                             caption=caption,
                             reply_markup=kb.inline_kb_full)
    elif code == 7:
        await bot.send_photo(callback_query.from_user.id, scetch3,
                             reply_markup=kb.inline_kb_full)


# Создаем хэндлер для кнопки
@dp.message_handler(text='btn3')
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, price_list,
                         reply_to_message_id=message.message_id)


# Сохраняем тексты для хэндлеров
help_message = text(
    "Доступные команды:\n",
    "/start - сделать заказ",
    "/prclst - прайс-лист",
    "/video1 - танец",
    "/video2 - собачки",
    "/photo - картинка",
    "/user_about - информация о художнике",
    "/arts_about - информация об ограничениях в артах",
    "/donate - поддержать автора",
    "/crack - сообщить об ошибке",
    "/bank - доступные для оплаты банки",
    "/otziv - оставить отзыв о боте",
    "/contact - мои контакты",
    "/anon - анонимные сообщения",
    sep="\n"
)

user_about_message = text(
    "Я Хастр (или же просто Настя). Мне 18 лет. Занимась рисованием "
    "уже 3-4 года и постоянно разиваюсь в этом направлении. "
    "Рисую в CSP. Буду рада видеть каждого!"
)

arts_about_message = text(
    "Рисую: разное, уточнять в лс"
    "\nНе рисую: 18+ контент, животных (только за доп плату), "
    "фетиши, сложные фоны (уточнять в лс), фурри"
)

donate_message = text(
    "Денюжки автору на покушать (только по желанию!)"
    "\nТинькофф: 2200700798201868"
    "\nСбер: 2202202630653958"
    "\nБусти:"
)

crack_message = text(
    "Если заметил где-то ошибку/проблему/недочет "
    "в боте, "
    "то напиши, пожалуйста, об этом."
    "\n(начни с ""Пофикси"")"
)

bank_message = text(
    "Доступные банки для оплаты на данный момент: "
    "Тинькофф, Сбер."
    "\nДоступна оплата через Бусти."
)

otziv_message = text(
    "Здесь ты можешь написать о работе бота "
    "и своих пожеланиях к его работе!"
    "\n(начни с ""Отзыв"")"
)

contact_message = text(
    "Мои контакты:"
    "\nпочта - bezumovaas@gmail.com"
    "\nтг - @hastr_xxx"
    "\nвк - @hasssstr"
)

anon_message = text(
    f"По этой ссылке ты можешь написать мне анонимно: "
    f"https://t.me/anonim_mail_bot?start=5037378984"
)

otzivz_zakaz = text(
    "Здесь ты можешь написать о полученном"
    "заказе!"
    "\n(начни с ""О заказе"")"
)

# Создаем хэндлер команды help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message,
                        reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды photo
@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, fff,
                         reply_to_message_id=message.message_id,
                         reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды prclst
@dp.message_handler(commands=['prclst'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, price_list,
                         reply_to_message_id=message.message_id,
                         reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды video1
@dp.message_handler(commands=['video1'])
async def process_video_command(message: types.Message):
    await bot.send_video(message.from_user.id, v2,
                         reply_to_message_id=message.message_id,
                         reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды video2
@dp.message_handler(commands=['video2'])
async def process_video_command(message: types.Message):
    await bot.send_video(message.from_user.id, v1,
                         reply_to_message_id=message.message_id,
                         reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды user_about
@dp.message_handler(commands=['user_about'])
async def process_help_command(message: types.Message):
    await message.reply(user_about_message,
                        reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды arts_about
@dp.message_handler(commands=['arts_about'])
async def process_help_command(message: types.Message):
    await message.reply(arts_about_message,
                        reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды donate
@dp.message_handler(commands=['donate'])
async def process_help_command(message: types.Message):
    await message.reply(donate_message,
                        reply_markup=kb.inline_kb_full)


# Создаем хэндлер команды crack
@dp.message_handler(commands=['crack'])
async def process_help_command(message: types.Message):
    await message.reply(crack_message,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер команды bank
@dp.message_handler(commands=['bank'])
async def process_help_command(message: types.Message):
    await message.reply(bank_message,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер команды otziv
@dp.message_handler(commands=['otziv'])
async def process_help_command(message: types.Message):
    await message.reply(otziv_message,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер команды contact
@dp.message_handler(commands=['contact'])
async def process_help_command(message: types.Message):
    await message.reply(contact_message,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер команды anon
@dp.message_handler(commands=['anon'])
async def process_help_command(message: types.Message):
    await message.reply(anon_message,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер команды otzivz_zakaz
@dp.message_handler(commands=['otzivz_zakaz'])
async def process_help_command(message: types.Message):
    await message.reply(otzivz_zakaz,
                        reply_markup=kb.inline_kb_full)

# Создаем хэндлер для нежданных сообщений
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    m = msg.text
    if m[:5] == 'Заказ':
        message_text = text('Спасибо за заказ!\n'
                            'Скоро тебе напишут в лс для уточнения деталей')
        await msg.reply(message_text,
                        parse_mode=ParseMode.MARKDOWN)
    elif m[:7] == 'Пофикси':
        message_text = text('Спасибо за обратную связь!\n'
                            'В скором времени постараюсь все исправить')
        await msg.reply(message_text,
                        parse_mode=ParseMode.MARKDOWN)
    elif m[:5] == 'Отзыв':
        message_text = text('Спасибо за отзыв!')
        await msg.reply(message_text,
                        parse_mode=ParseMode.MARKDOWN)
    elif m[:8] == 'О заказе':
        message_text = text('Спасибо за отзыв! Буду рада сотрудничать снова!')
        await msg.reply(message_text,
                        parse_mode=ParseMode.MARKDOWN)
    else:
        message_text = text(('Хорошая попытка!'),
                            italic('\nНо просто напомню,'), 'что есть',
                            code('команда'), '/help')
        await msg.reply(message_text,
                        parse_mode=ParseMode.MARKDOWN)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    executor.start_polling(dp)