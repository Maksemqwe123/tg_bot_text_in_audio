from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from gtts import gTTS

from button import *

BOT_TOKEN = '5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg'


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class TextaudioRu(StatesGroup):
    audio_pleas = State()


class TextaudioEn(StatesGroup):
    audio_pleas_en = State()


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    welcome = message.from_user.full_name
    await message.answer(f'Привет {welcome}, Я бот который преобразует текст в аудиосообщение',
                         reply_markup=text_in_audio)


@dp.message_handler(Text(equals='Озвучить текст на русском🇷🇺', ignore_case=True))
async def text_audio(message: types.Message):
    await message.answer('Введите текст который нужно озвучить (на русском)')

    await TextaudioRu.audio_pleas.set()


@dp.message_handler(state=TextaudioRu.audio_pleas)
async def audio_user(message: types.Message, state: FSMContext):

    text_user = message.text

    audio = gTTS(text=text_user, lang='ru', slow=False)
    audio.save('audio.wav')

    await message.bot.send_audio(message.from_user.id, open('audio.wav', 'rb'), reply_markup=text_in_audio)

    await state.finish()


@dp.message_handler(Text(equals='Озвучить текст на англ🇬🇧', ignore_case=True))
async def text_audio_en(message: types.Message):
    await message.answer('Введите текст который нужно озвучить (на английском)')

    await TextaudioEn.audio_pleas_en.set()


@dp.message_handler(state=TextaudioEn.audio_pleas_en)
async def audio_user_en(message: types.Message, state: FSMContext):

    text_user = message.text

    audio = gTTS(text=text_user, lang='en', slow=False)
    audio.save('audio_en.wav')

    await message.bot.send_audio(message.from_user.id, open('audio_en.wav', 'rb'), reply_markup=text_in_audio)

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
