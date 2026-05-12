# keyboards.py
# Все клавиатуры (меню) бота — в одном месте.
# Функция возвращает готовую клавиатуру — хэндлер просто вызывает её.

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_main() -> InlineKeyboardMarkup:
    """
    Главное меню. Вызывается при /start и по кнопке «Назад».
    builder.adjust(1) — каждая кнопка на отдельной строке.
    """
    builder = InlineKeyboardBuilder()
    # text — надпись на кнопке
    # callback_data — строка, которую получит бот при нажатии (до 64 байт)
    builder.button(text="📖 О боте",      callback_data="about")
    builder.button(text="🆘 Помощь",      callback_data="help")
    builder.button(text="🐈‍⬛ GITHUB",    callback_data="git")
    builder.button(text="🦎 ИТД", callback_data="itd")
    builder.adjust(2,2)  # по 2 кнопки в ряд
    return builder.as_markup()


def menu_back() -> InlineKeyboardMarkup:
    """
    Кнопка «Назад» — возвращает в главное меню.
    Используется на каждой внутренней странице.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="← Назад", callback_data="main")
    return builder.as_markup()
