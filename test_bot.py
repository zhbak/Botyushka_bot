from answer.gpt_eleven import gpt_message, audio_generation
from dotenv import load_dotenv
import os, time, telebot

load_dotenv()
bot_token = os.environ.get("BIBLE_BOT_TOKEN")

bot = telebot.TeleBot(bot_token)
user_status = {}

# Стартовая функция
@bot.message_handler(commands=['start'])
def start(message : telebot.types.Message):

    start_text = '''
Доброго дня, {}! 
Я ботюшка \u271D.
Помогу твоей душе. 
Напиши что тебя беспокоит или задай вопрос.
    '''.format(message.from_user.first_name)

    bot.send_message(message.chat.id, start_text)

@bot.message_handler(content_types=['text'])
# Выполнение функции
def batuska_answer(message : telebot.types.Message):
    try:
        bot.reply_to(message, "Вспоминаю Библию... ⏳")
        output = gpt_message(message)
        #audio_generation(output)
        #with open('audio.mp3', 'rb') as audio_file:
         #       # Отправляем голосовое сообщение пользователю
          #      bot.send_voice(message.chat.id, audio_file)
        bot.reply_to(message, """{}""".format(output))
    except Exception as e:
        bot.reply_to(message, """Ботюшка в отпуске \U0001F680. Заходи через месяц.""")
        print(e)

if __name__ == "__main__":
    print('Bot started.')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Exception occurred: {e}")
            time.sleep(15)  # Пауза перед следующей попыткой