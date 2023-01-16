from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

text_in_audio = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton('Озвучить текст на русском🇷🇺'),
    KeyboardButton('Озвучить текст на англ🇬🇧')
)
