import telebot
from telebot import types
from config import token


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['help'])
def send_text(message):
    bot.send_message(message.chat.id, 'Стоимость лекарств можно посмотреть здесь: https://tabletka.by/')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nos_btn = types.KeyboardButton("Заложен нос")
    sinusit_btn = types.KeyboardButton("Лечение синуситов")
    prostuda_btn = types.KeyboardButton("Простуда")
    yho_btn = types.KeyboardButton("Болит ухо")
    gorlo_btn = types.KeyboardButton("Болит горло")
    kashel_btn = types.KeyboardButton("Кашель")
    diareya_btn = types.KeyboardButton("Заболевания желудочно-кишечного тракта")
    high_ad_btn = types.KeyboardButton("Высокое артериальное давление")
    pain_btn = types.KeyboardButton("Головная,мышечная,зубная боль")

    markup.add(nos_btn, sinusit_btn, prostuda_btn, yho_btn, gorlo_btn, kashel_btn, diareya_btn, high_ad_btn, pain_btn)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Заложен нос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            prom_nos = types.KeyboardButton("Для промывания носа")
            sosud = types.KeyboardButton("Сосудосуживающие капли")
            back = types.KeyboardButton("Назад")
            markup.add(prom_nos, sosud, back)

            bot.send_message(message.chat.id, "Заложен нос", reply_markup=markup)
        elif message.text == "Для промывания носа":
            bot.send_message(message.chat.id, "ПРОМЫВАЙТЕ НОС \n"
                                              "Для этого вы можете использовать:\n"
                                              "На основе морской воды:\n"
                                              "1)Аква марис(Хорватия).Аналоги:Аквалор(Швеция),Квикс(Германия),Humer(Франция)\n"

                                              "На основе физиологического раствора:\n"
                                              "1)Салин(Германия).Аналоги:Аквасол(РБ),Ринолюкс(РБ)\n"
                                              "По три впрыскивания 2-3 раза в день в каждый носовой ход\n")
            img = open("picture/kviks-akvamaris.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Для промывания носа")
            img.close()
        elif message.text == "Сосудосуживающие капли":
            bot.send_message(message.chat.id, "Сосудосуживающие капли:\n"
                                              "__Действуют до 8 часов:__\n"
                                              "1)Снуп(Германия).Аналоги:Отривин(Швейцария),Ринол(РБ),Ксиназол(РБ),Рино Марис(в комбинации с морской водой)(Хорватия)\n"
                                              "2)Галазолин Комби(Польша)-увлажняет слизистую благодаря наличию декспантенола\n"
                                              "Действуют до 10-12 часов:\n"
                                              "1)Назол(Италия).Аналоги:Нозакар(Палестина),Ноксивин(РБ),Рузана(РБ)\n"

                                              "По 1 впрыскиванию 2 раза в сутки.Пользоваться не более 7 дней")
            img = open("picture/nasol.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Пользоваться не более 7 дней")
            img.close()
        elif message.text == "Лечение синуситов":
            bot.send_message(message.chat.id,
                             "Таблетки Синупрет.Принимать по 2 таблетки 3 раза в день.Запивать большим количеством воды.\n"
                             "Таблетки синупрет форте(или экстракт).Принимать по 1 таблетке 3 раза в день.\n"
                             "Сироп синупрет принимать 7 мл 3 раза в день.\n"
                             "Капли синупрет принимать 50 капель 3 раза в день.\n")
            img = open("picture/sin.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Таблетки Синупрет.Принимать по 2 таблетки 3 раза в день.Запивать большим количеством воды.\n")
            img.close()

        elif message.text == "Простуда":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            prot_vir = types.KeyboardButton("Противовирусные лс")
            simptom = types.KeyboardButton("Порошки для снятия симптомов")
            back = types.KeyboardButton("Назад")
            markup.add(prot_vir, simptom, back)

            bot.send_message(message.chat.id, "Простуда", reply_markup=markup)
        elif message.text == "Противовирусные лс":
            bot.send_message(message.chat.id, "Для лечения: \n"
                                              "1)Флустоп(РБ) с 13 лет.Аналоги:Тамифлю(США),Осельтамивир(Индия),Тами-грипп(Польша):\n"
                                              "Принимать по одной капсуле 2 раза в день в течение 5 дней.\n"
                                              "Для профилактики постконтактной при тесном контакте с больным:1 капсула 1 раз в день в течение 10 дней.\n"
                                              "2)Витавирин(РБ) с 18 лет.Аналоги:(Ингавирин в капсулах)(Россия).Принимать по 1 порошку 1 раз в день.\n"
                                              "3)Гроприносин(Венгрия) с 1 года.Аналоги:Иммунозин(РБ).Принимать по 2 таблетки 3 раза в сутки в течение 14 дней.\n"
                                              "4)Амизон(Украина) с 18 лет.Принимать по 2 таблетки 3 раза в день.Противопоказание-заболевание щитовидной железы.\n"
                                              "5)Амизон макс(Украина) с 18 лет.Принимать по 1 капсуле 3 раза в день.Противопоказание-заболевание щитовидной железы.\n"
                                              "6)Полиоксидоний(Россия) с 12 лет.Иммуномодулятор.Комплексная терапия ОРВИ.\n"
                                              "Принимать по 1 таблетке 1-3 раза в день в течение 10 дней за 30 минут до еды.\n")
            img = open("picture/tam.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Для лечения гриппа.По 1 капсуле 2 раза в день в течение 5 дней")
            img.close()


        elif message.text == "Порошки для снятия симптомов":
            bot.send_message(message.chat.id,"Порошок растворить в стакане с горячей водой.Принимать не более 4 пакетиков в день \n"
                             "1)Терафлю(Франция)(С 12 лет).Аналоги:Тайлол фен Хот(Турция),Антигриппин(Польша),Гриппомикс(РБ),Ангриколд(РБ)\n"
                             "2)Инсти(Пакистан)(с 18 лет)-в составе содержатся травы:Ива,солодка.\n"
                             "3)Гриппостад С(Германия)(с 15 лет)Ангримакс(РБ).Принимать по 2 капсулы 3 раза в день.\n"
                             "4)Ринзип(РБ) (с 15 лет)1 таблетка 3 раза в сутки.Принимать не более 5 дней")

            img = open("picture/ter.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="В составе есть парацетамол.Не более 4 порошков в день")
            img.close()

        elif message.text == "Болит ухо":
            bot.send_message(message.chat.id,
                             "1)Отипакс(Франция)-оказывает противовоспалительное и анальгезирующее действие.\n"
                             "Аналоги:Отирелакс(Румыния),Отис(РБ),Отисфен(РБ).Закапыать в слуховой проход 2-3 раза в день3-4 капли.\n"
                             "Перед применением согреть в ладонях.Применять не более 10 дней.\n"
                             "2)Анауран(Италия)-антибиотик с обезболивающим.При остром отите закапывать по 4 капли 3 раза в день\n")

            img = open("picture/otipax.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="3 капли 2 раза в день")
            img.close()

        elif message.text == "Болит горло":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            tab_gorlo = types.KeyboardButton("Таблетки для рассасывания")
            sprey = types.KeyboardButton("Спрей для горла")
            back = types.KeyboardButton("Назад")
            markup.add(tab_gorlo, sprey, back)

            bot.send_message(message.chat.id, "Болит горло", reply_markup=markup)

        elif message.text == "Таблетки для рассасывания":
            bot.send_message(message.chat.id,
                             "Першение в горле:1)Гексализ(Франция)(с 6 лет).Оказывает противовоспалительное действие.По 1 таблетке 6 раз в день.\n"
                             "2)Эфизол(Болгария)(с 4 лет).Антисептическое и противогрибковое действие.По 1 таблетке каждые 3 часа.\n"
                             "3)Лорсепт(РБ)(с 6 лет).Антисептическое действие.Рассасывать по 1 таблетке каждые 3 часа.\n"
                             "Боль в горле:1)Граммидин Нео с анестетиком(Россия)(с 6 лет).В составе антибиотик местного действия.По 1 таблетке 3 раза в день не более 7 дней.\n"
                             "2)Септолете Тотал(Словения)(с 6 лет)Антисептическое  и анальгезирующее действие.Рассасывать по 1 таблетке каждые 3 часа.\n")
            img = open("picture/grammidin.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 1 таблетке 3 раза в день.Не более 7 дней")
            img.close()

        elif message.text == "Спрей для горла":
            bot.send_message(message.chat.id,
                             "1)Орасепт(Щвейцария)Аналоги: Оросептин(РБ)(С 3 лет).Антисептическое действие.По 2 орошения 4 раза в день.\n"
                             "2)Гексаспрей(Франция)( с 6 лет).По 2 орошения 3 раза в день.\n"
                             "3)Септолете плюс(Словения)(с 12 лет).По 2 орошения 3 раза в день.\n")
            img = open("picture/hexasprey.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 2 орошения 3 раза в день")
            img.close()

        elif message.text == "Кашель":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            vl_kashel = types.KeyboardButton("Кашель с мокротой")
            suh_kashel = types.KeyboardButton("Сухой кашель")
            back = types.KeyboardButton("Назад")
            markup.add(vl_kashel, suh_kashel, back)

            bot.send_message(message.chat.id, "Кашель", reply_markup=markup)
        elif message.text == "Кашель с мокротой":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            sirop = types.KeyboardButton("Сиропы")
            tabletki = types.KeyboardButton("Таблетки")
            back = types.KeyboardButton("Назад")
            markup.add(sirop, tabletki, back)
            bot.send_message(message.chat.id, "Кашель с мокротой", reply_markup=markup)
        elif message.text == "Сиропы":
            bot.send_message(message.chat.id,
                             "1)Лазолван 30 мг/5 мл(Франция).Аналоги:Амброгексал(Германия),Халиксол(Венгрия),Амбровикс(РБ).\n"
                             "Принимать по 5 мл 3 раза в день\n"
                             "2)Проспан(Германия)на основе плюща.Аналоги:Геделикс(Германия),Пектолван(Украина).По 5 мл 3 раза в день.\n"
                             "3)Гербапект(Польша) растительный состав.По 5 мл 3 раза в день.\n"
                             "Если мокрота отходит очень тяжело:\n"
                             "Флюдитек 5% (Франция)(с 15 лет).По 15 мл 3 раза в день, желательно за 1 час до еды или через 2 часа после еды.")
            img = open("picture/lazolvsn.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 5 мл 3 раза в день")
            img.close()

        elif message.text == "Таблетки":
            bot.send_message(message.chat.id,
                             "Лазолван(Франция)(с 6 лет)Аналоги:Халиксол(Германия),Абровикс(РБ),Флавамед(Германия).По 1 таблетке 3 раза в день.\n"
                             "Пастилки для рассасывания:Гербион  плющ(Словения)( с 6 лет).По 1 пастилке 3 раза в день.\n"
                             "Если мокрота отходит очень тяжело:АЦЦ ЛОНГ(с 12 лет).По 1 шипучей таблетке 1 раз в день")
            img = open("picture/ambro.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 1 таблетке 3 раза в день")
            img.close()

        elif message.text == "Сухой кашель":
            bot.send_message(message.chat.id,
                             "Сиропы,которые переводят сухой кашель во влажный:"
                             "1)Гербион с исландским мхом(Словения)(с 12 лет).По 15 мл 4 раза в сутки.\n"
                             "Пастилки для рассасывания:Исла-минт,Исла-моос(Германия)(с 6 лет).По 1 пастилке 3 раза в сутки.\n")

            img = open("picture/ger.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 15 мл 4 раза в день")
            img.close()

        elif message.text == "Заболевания желудочно-кишечного тракта":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            diareya = types.KeyboardButton("Диарея")
            zapor = types.KeyboardButton("Запор")
            back = types.KeyboardButton("Назад")
            markup.add(diareya, zapor, back)
            bot.send_message(message.chat.id, "Заболевания желудочно-кишечного тракта", reply_markup=markup)

        elif message.text == "Диарея":
            bot.send_message(message.chat.id,
                             "1)Смекта(Франция)(с 2 лет)Аналоги:Смектика(РБ).Взрослым принимать до 6 пакетиков в день,растворив в воде комнатной температуры.\n"
                             "2)Если диарея неинфеционная.Лопедиум(Германия)(с 6 лет)Аналоги:Ларемид(Польша)Лоперамид(РБ).\n"
                             "Принимать 2 капсулы, затем по 1 капсуле  после каждого акта дефекации.\n"
                             "3)Стопдиар(Польша)Аналоги:Нифуроксазид(РБ).По 2 таблетки по 100 мг 4 раза/сут.\n")

            img = open("picture/smecta.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 1 пакетику 4 раза в день")
            img.close()

        elif message.text == "Запор":
            bot.send_message(message.chat.id,
                             "1)Дюфалак(Нидерланды)(с рождения)Аналоги:Лактулоза(РБ).Принимать по 15 мл 3 раза в день.")

            img = open("picture/dufalak.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="По 1 пакетику 4 раза в день")
            img.close()

        elif message.text == "Высокое артериальное давление":
            bot.send_message(message.chat.id,
                             "1)Блокордил 25 мг принимать под язык.Аналоги:Каптоприл(РБ).При необходимости принять вторую таблетку.\n")

            img = open("picture/blocordil.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="При высоком давлении")
            img.close()

        elif message.text == "Головная,мышечная,зубная боль":
            bot.send_message(message.chat.id,
                             ":1)Темпалгин(Болгария)(с 15 лет)\n"
                             "2)Кеторол(Индия)Аналоги:Кеторолак(РБ)(с 16 лет)\n"
                             "3)Аэртал(Венгрия(с 18 лет)\n"
                             "4)Вольтарен(Швейцария)(с 12 лет)Аналоги:Диклофенак(РБ).Принимать не более 3 таблеток в день.Не более 5 дней")

            img = open("picture/ketorol.jpg.", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="До 3 таблеток в день,не более 5 дней")
            img.close()

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            nos_btn = types.KeyboardButton("Заложен нос")
            sinusit_btn = types.KeyboardButton("Лечение синуситов")
            prostuda_btn = types.KeyboardButton("Простуда")
            yho_btn = types.KeyboardButton("Болит ухо")
            gorlo_btn = types.KeyboardButton("Болит горло")
            kashel_btn = types.KeyboardButton("Кашель")
            diareya_btn = types.KeyboardButton("Заболевания желудочно-кишечного тракта")
            high_ad_btn = types.KeyboardButton("Высокое артериальное давление")
            pain_btn = types.KeyboardButton("Головная,мышечная,зубная боль")

            markup.add(nos_btn, sinusit_btn, prostuda_btn, yho_btn, gorlo_btn, kashel_btn, diareya_btn, high_ad_btn,
                       pain_btn)

            bot.send_message(message.chat.id, "Назад", reply_markup=markup)


bot.polling(none_stop=True)
