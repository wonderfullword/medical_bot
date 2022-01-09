import telebot
from telebot import types


token="5006043369:AAFq08txl0nrBgJMNNlYtzBlD5LZ05859Sk"
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    nos_btn=types.KeyboardButton("Заложен нос")
    prostuda_btn=types.KeyboardButton("Простуда")
    yho_btn=types.KeyboardButton("Болит ухо")
    gorlo_btn=types.KeyboardButton("Болит горло")
    kashel_btn= types.KeyboardButton("Кашель")
    diareya_btn=types.KeyboardButton("Заболевания желудочно-кишечного тракта")
    high_ad_btn= types.KeyboardButton("Высокое артериальное давление")
    pain_btn = types.KeyboardButton("Головная,мышечная,зубная боль")

    markup.add(nos_btn,prostuda_btn, yho_btn, gorlo_btn, kashel_btn, diareya_btn, high_ad_btn, pain_btn)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Заложен нос":
            bot.send_message(message.chat.id, "ПРОМЫВАЙТЕ НОС \n"
                                              "Для этого вы можете использовать:\n"
            "На основе морской воды:\n"
            "1)Аквамарис\n"
            "2)Аквалор\n"
            "3)Квикс\n"
            "4)Humer\n"
            "На основе физиологического раствора:\n"
            "1)Аквасол \n"
            "2)Ринолюкс\n"
            "3)Салин\n"
            "По три впрыскивания 2-3 раза в день в каждый носовой ход\n" 
                             
            "Сосудосуживающие капли:\n"
            "Действуют до 8 часов:\n"
            "1)Снуп(Германия)\n"
            "2)Галазолин Комби(Польша)-увлажняет слизистую благодаря наличию декспантенола\n"
            "3)Отривин(Швейцария)\n"
            "4)Ринол(РБ)\n"
            "5)Ксиназол(РБ)\n"
            "6)Ксилин(РБ)\n"
            "7)Ринол(РБ)\n"
            "8)Рино Марис(в комбинации с морской водой)(Хорватия)\n"
                                              "Действуют до 10-12 часов:\n"
                                              "1)Назол(Италия)\n"
                                              "2)Нозакар(Палестина)\n"
                                              "3)Ноксивин(РБ)\n"
                                              "4)Рузана(РБ)\n"
            "__По 1 впрыскиванию 2 раза в сутки.Пользоваться не более 7 дней__")

        elif message.text=="Простуда":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            prot_vir = types.KeyboardButton("Противовирусные лекарственные средства")
            simptom = types.KeyboardButton("Порошки для снятия симптомов")
            back = types.KeyboardButton("Назад")
            markup.add(prot_vir, simptom, back)

            bot.send_message(message.chat.id,"Простуда", reply_markup=markup)


        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            nos_btn = types.KeyboardButton("Заложен нос")
            prostuda_btn = types.KeyboardButton("Простуда")
            yho_btn = types.KeyboardButton("Болит ухо")
            gorlo_btn = types.KeyboardButton("Болит горло")
            kashel_btn = types.KeyboardButton("Кашель")
            diareya_btn = types.KeyboardButton("Заболевания желудочно-кишечного тракта")
            high_ad_btn = types.KeyboardButton("Высокое артериальное давление")
            pain_btn = types.KeyboardButton("Головная,мышечная,зубная боль")

            markup.add(nos_btn, prostuda_btn, yho_btn, gorlo_btn, kashel_btn, diareya_btn, high_ad_btn, pain_btn)

            bot.send_message(message.chat.id, "Назад", reply_markup=markup)


bot.polling(none_stop=True)