import os
import telebot

# Бот берёт токен из секретных настроек хостинга
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Реакция на команду /start
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(
        message.chat.id, 
        "🛰️ **[ТЕРМИНАЛ FERRERO TEAM]**\n\nСистема готова к работе. Введите код с найденной флешки:"
    )

# Проверка введённого кода
@bot.message_handler(func=lambda message: True)
def check_code(message):
    user_code = message.text.strip().upper()
    
    if user_code == "LAB-101":
        bot.send_message(
            message.chat.id, 
            "🔓 **ДОСТУП РАЗРЕШЁН**\n\n*Расшифровка лога #01:*\n«Объект пробил защиту в секторе Б. Персоналу немедленно эвакуироваться.»"
        )
    else:
        bot.send_message(message.chat.id, "❌ **ОШИБКА:** Код не найден в базе данных.")

if __name__ == '__main__':
    print("Бот успешно запущен!")
    bot.infinity_polling()
