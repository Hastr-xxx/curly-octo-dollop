from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Хочу сделать заказ!')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)


inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_btn_2 = InlineKeyboardButton('Сделать заказ :3', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('Прайс лист', callback_data='btn3')
inline_kb_full.add(inline_btn_2, inline_btn_3)
inline_kb_full.add(InlineKeyboardButton('Обратная связь', url='https://t.me/hastr_xxx'))