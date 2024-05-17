from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подробная информацио о работе отделов ЗАГС Калининградской области"),          
        ],
        [
            KeyboardButton(text="Получение справок/свидетельств"),
            KeyboardButton(text="Госрегистрация актов"),
        ],
        [
            KeyboardButton(text="Cоциальные сети"),
            KeyboardButton(text="Апостиль")
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

gosregacts = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рождение"),
            KeyboardButton(text="Установление отцовства"),
        ],
        [
            KeyboardButton(text="Заключение брака"),
            KeyboardButton(text="Расторжение брака"),
        ],
        [
            KeyboardButton(text="Усыновление / Удочерение"),
            KeyboardButton(text="Перемена имени"),
        ],
        [
            KeyboardButton(text="Внесение изменений в акты"),
            KeyboardButton(text="Смерть"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что именно вы хотите сделать?'
)

Rastorjenie_braka_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кто может получить услугу?"),
            KeyboardButton(text="Перечень документов"),
            KeyboardButton(text="Государственная пошлина"),
        ],
        [
            KeyboardButton(text="Способы обращения"),
            KeyboardButton(text="Срок предоставления"),
            KeyboardButton(text="Вернуться в главное меню"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что именно вы хотите сделать?'
)


Zakluchenie_braka_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кто может получить услугу?"),
            KeyboardButton(text="Перечень документов"),
            KeyboardButton(text="Государственная пошлина"),
        ],
        [
            KeyboardButton(text="Способы обращения"),
            KeyboardButton(text="Срок предоставления"),
            KeyboardButton(text="Вернуться в главное меню"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что именно вы хотите сделать?'
)

