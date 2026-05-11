# 🤖 ToolsBot
Бот для личного использоввания. Предназначен чтобы быстро получать доступ к нужным сайтам.


## Возможности

- Быстрый доступ к github  и великолепной сотсети ильи nowkie



## Технологии

- Python 3.x
- [aiogram](https://docs.aiogram.dev/) — фреймворк для Telegram ботов

## Установка и запуск

1. Клонируй репозиторий:
```bash
   git clone https://github.com/твойник/telegram-bot.git
   cd telegram-bot
```

2. Установи зависимости:
```bash
   pip install -r requirements.txt
```

3. Создай файл `.env` и добавь свой токен: 
BOT_TOKEN=твой_токен_здесь

4. Запусти бота:
```bash
   python bot.py
```

## Структура проекта
├── bot.py          # Основной файл, точка входа
├── handlers.py     # Обработчики команд и сообщений
├── keyboards.py    # Кнопки
└── .env            # Токен (не публикуется)