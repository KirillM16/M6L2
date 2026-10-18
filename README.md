# Telegram Image Bot

Простой Telegram-бот, который генерирует изображения по текстовому описанию с помощью Pollinations AI.

Пользователь отправляет команду `/image` и описание картинки, а бот возвращает сгенерированное изображение.

## Возможности

- Генерация изображений по промту
- Отправка готового фото прямо в чат
- Работа через Telegram Bot API
- Использует API Pollinations AI

## Технологии

- Python
- pyTelegramBotAPI (`telebot`)
- requests
- Pollinations AI API

## Установка

1. Клонируй репозиторий:

```bash
git clone [https://github.com/ТВОЙ_НИК/telegram-image-bot.git](https://github.com/ТВОЙ_НИК/telegram-image-bot.git)
cd telegram-image-bot
```

2. Установи зависимости:

```bash
pip install -r requirements.txt
```

Если файла `requirements.txt` нет:

```bash
pip install pyTelegramBotAPI requests
```

3. Создай файл `config.py`:

```python
BOT_TOKEN = "токен_твоего_бота"
API_KEY = "ключ_Pollinations"
```

Токен бота можно получить у [@BotFather](https://t.me/BotFather).

## Запуск

```bash
python bot.py
```

## Использование

Отправь боту команду:

```text
/image кот в космосе
```

Бот сгенерирует изображение и отправит его в чат.

## Структура проекта

```text
.
├── bot.py               # код Telegram-бота
├── image_generator.py   # генерация изображений
├── config.py            # токены и ключи
├── requirements.txt     # зависимости
└── README.md
```

## Безопасность

Не публикуй `config.py`, `BOT_TOKEN` и `API_KEY` в репозитории.

Добавь в `.gitignore`:

```gitignore
config.py
__pycache__/
*.jpg
*.png
```

## Лицензия

Проект распространяется по лицензии MIT.
