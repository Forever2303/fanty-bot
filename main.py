import telebot
import random

# Вставь свой токен бота сюда
TOKEN = '8308287454:AAGgA6APNYVOc7b75_LUeHPG5CYO-k2LcH8 '
bot = telebot.TeleBot(TOKEN)

# Список заданий (фанты)
tasks = [
    "Станцуй танец курицы",
    "Спой куплет любой песни",
    "Расскажи анекдот",
    "Изобрази кота, просящего еду",
    "Сделай 10 приседаний",
    "Промяукай своё имя",
    "Признайся в любви первому человеку в чате",
    "Поменяй аватарку на смешную на 10 минут",
    "Расскажи секрет (можно вымышленный)",
    "Сделай комплимент каждому участнику чата"
]

# Команда старта
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для игры в фанты 🎉\nНапиши /fant чтобы получить задание.")

# Команда "фант"
@bot.message_handler(commands=['fant'])
def send_task(message):
    task = random.choice(tasks)
    bot.send_message(message.chat.id, f"🎲 Твое задание: {task}\n\nПрими вызов? 😉")

# Обработка любых других сообщений
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.text.lower() in ["да", "принимаю", "выполню", "ок"]:
        bot.reply_to(message, "Отлично! Ждём исполнения 😄")
    elif message.text.lower() in ["нет", "отказываюсь", "не буду"]:
        bot.reply_to(message, "Жаль! Может в следующий раз 🙃")

# Запуск бота
print("Бот запущен...")
bot.infinity_polling()
