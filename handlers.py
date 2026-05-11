# handlers.py
# Все обработчики бота.
# Главная идея меню: не отправлять новое сообщение, а редактировать старое.
# Это делает edit_text() — текст и кнопки меняются, сообщение остаётся одно.

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

# Импортируем только то, что создали в keyboards.py
from keyboards import menu_main, menu_back

# Router — контейнер хэндлеров.
# bot.py подключит его через dp.include_router(router)
router = Router()


# ── /start ────────────────────────────────

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Точка входа. Отправляет приветствие и главное меню.
    answer() — новое сообщение (здесь это нужно, т.к. ещё нечего редактировать).
    reply_markup — прикрепляет клавиатуру к сообщению.
    """
    await message.answer(
        "👋 Добро пожаловать!\n\nВыбери раздел:",
        reply_markup=menu_main()
    )


# ── Кнопка «О боте» ───────────────────────

@router.callback_query(F.data == "about")
async def on_about(callback: CallbackQuery):
    """
    Срабатывает при нажатии кнопки с callback_data="about".

    callback.answer() — ОБЯЗАТЕЛЕН. Убирает анимацию загрузки с кнопки.
    Без него Telegram будет крутить часики 30 секунд.

    callback.message.edit_text() — редактирует то же сообщение.
    Это ключевой приём меню: одно сообщение «трансформируется» между разделами,
    а не появляется куча новых сообщений в чате.
    """
    await callback.answer()  # убираем анимацию с кнопки
    await callback.message.edit_text("📖О боте\n" "Я бот для быстрого доступа к нужным сервисам\n",
        reply_markup=menu_back()  # показываем кнопку «Назад»
    )


# ── Кнопка «Помощь» ───────────────────────

@router.callback_query(F.data == "help")
async def on_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "🆘 Помощь\n"
        "Её не будет лол, терпи.\n",
        reply_markup=menu_back()
    )


# ── Кнопка «GIT» ─────────────────────

@router.callback_query(F.data == "git")
async def on_git(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "🌐 Типа разработчик?, типа крутой?\n"
        "Github: https://github.com\n",
        reply_markup=menu_back()
    )

# ── Кнопка «ИТД» ─────────────────────

@router.callback_query(F.data == "itd")
async def on_itd(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "БОЖЕ ДА СТАНЬ ЧАСТЬЮ ИТД, ПРИМКНИ К ПРОЕКТУ ЛУЧШЕГО SEO Ильи nowkie и тд\n"
        "ИТД: https://итд.com/\n",
        reply_markup=menu_back()
    )




# ── Кнопка «Назад» ────────────────────────

@router.callback_query(F.data == "main")
async def on_back(callback: CallbackQuery):
    """
    Возврат в главное меню.
    Снова edit_text() — редактируем то же сообщение обратно.
    """
    await callback.answer()
    await callback.message.edit_text(
        "👋 Добро пожаловать!\n\nВыбери раздел:",
        reply_markup=menu_main()
    )
