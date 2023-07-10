from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"""
    Рад вас видеть, {message.from_user.full_name}! Я - бот для поиска отелей. 
Я умею:

1. Выводить основную информацию об отели и его фотографии 

2. Отправить вам ссылку на отель для прямого бронирования!

3. Сохранять историю поиска
    
И другие полезные операции!
    
Чтобы узнать все мои команды, введи /help
    """)

