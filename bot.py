import telebot
from telebot import types

token="5006043369:AAFq08txl0nrBgJMNNlYtzBlD5LZ05859Sk"
bot=telebot.TeleBot(token)

def create_keyboard():
    keyboard=types.InlineKeyboardMarkup()
    prostuda_btn=types.InlineKeyboardButton(text="Простуда",callback_data="1")
    nos_btn=types.InlineKeyboardButton(text="Заложен нос",callback_data="2")
    yho=types.InlineKeyboardButton(text="Болит ухо", callback_data="3")
    gorlo= types.InlineKeyboardButton(text="Болит горло", callback_data="4")
    kashel= types.InlineKeyboardButton(text="Кашель", callback_data="5")
    diareya= types.InlineKeyboardButton(text="Заболевания желудочно-кишечного тракта", callback_data="6")
    high_ad= types.InlineKeyboardButton(text="Высокое артериальное давление", callback_data="7")
    pain= types.InlineKeyboardButton(text="Головная,мышечная,зубная боль", callback_data="8")
    keyboard.add(prostuda_btn)
    keyboard.add(nos_btn)
    keyboard.add(yho)
    keyboard.add(gorlo)
    keyboard.add(kashel)
    keyboard.add(diareya)
    keyboard.add(high_ad)
    keyboard.add(pain)
    return keyboard
@bot.message_handler(commands=["start"])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день!Выберите,что вас беспокоит",
        reply_markup=keyboard
    )
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard=create_keyboard()
    if call.message:
        if call.data=="1":
            img=open("orvi.jpg","rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка орвиколд",
                reply_markup=keyboard)
            img.close()

        if call.data == "2":
            img = open("sin.jpg", "rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка синупрет",
                reply_markup=keyboard)
            img.close()



if __name__=="__main__":
    bot.polling(none_stop=True)