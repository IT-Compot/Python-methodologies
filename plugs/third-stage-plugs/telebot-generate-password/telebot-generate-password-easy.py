import telebot  # pyTelegramBotAPI
import random
import string

# --- Конфигурация ---
BOT_TOKEN = "ТОКЕН"

# --- Инициализация бота ---
bot = telebot.TeleBot(BOT_TOKEN)


# --- Вспомогательные функции ---
def generate_password(length: int, char_set_code: int) -> str:
    """Генерирует пароль на основе заданной длины и набора символов."""

    # По желанию можно добавить или убрать усливия ниже
    
    if char_set_code == 1:
        characters = string.digits
    elif char_set_code == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits

    if length <= 0 or length > 100:
        return "Ошибка: Длина должна быть от 1 до 100."

    # password = ''.join(random.choice(characters) for _ in range(length)) # Тоже самое, что и ниже
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# --- Обработчики команд ---

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение."""
    bot.reply_to(message,
                 "Привет! Я бот-генератор случайных паролей.\n\n"
                 "Используй команду:\n"
                 "/generate <длина> <набор_символов>\n\n"
                 "Наборы символов (примеры):\n"
                 "  1: только цифры (0123456789)\n"
                 "  2: буквы + цифры\n"
                 )


# Команда /generate
@bot.message_handler(commands=['generate'])
def generate_password_command(message):
    """Обработчик команды /generate."""

    # Разбиваем текст сообщения на слова (аргументы)
    # message.text содержит весь текст сообщения, включая команду
    parts = message.text.split()

    # Удаляем команду, оставляем только аргументы
    # parts[0] - это '/generate'
    args = parts[1:]

    if len(args) != 2:
        bot.reply_to(message,
                     "Неверное количество аргументов. Используйте:\n"
                     "/generate <длина> <код_набора>\n"
                     "Пример: /generate 16 4")
        return
    # try, except изспользовать по желанию
    # С try и except
    try:
        length = int(args[0])
        char_code = int(args[1])

        # Генерируем пароль
        new_password = generate_password(length, char_code)

        # Отправляем ответ. Markdown для выделения пароля.
        bot.reply_to(message, f"Ваш новый пароль:\n`{new_password}`",
                     parse_mode='Markdown')

    except ValueError:
        bot.reply_to(message,
                     "Ошибка: Длина и код набора должны быть целыми числами.\n"
                     "Пример: /generate 12 3")
    except Exception as e:
        bot.reply_to(message, "Произошла внутренняя ошибка генерации.")

    # Без try и except

    # length = int(args[0])
    # char_code = int(args[1])

    # # Генерируем пароль
    # new_password = generate_password(length, char_code)

    # # Отправляем ответ. Markdown для выделения пароля.
    # bot.reply_to(message, f"Ваш новый пароль:\n`{new_password}`",
    #              parse_mode='Markdown')

# Обработчик для всех остальных текстовых сообщений (если нужно)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, "Я умею генерировать пароли по команде /generate. Для помощи введите /start.")

# --- Запуск бота ---
bot.infinity_polling()
