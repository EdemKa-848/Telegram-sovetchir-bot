import telebot
from telebot import types
from config import *
from logic_bot import DB_Manager
import telebot.types 
from telebot import types
from dopfunkcii import *


bot = telebot.TeleBot(TOKEN)
RECOMENDATION = {
    "Высокий доход:":" Рассмотрите профессии в таких сферах, как финансовый анализ или программирование, которые могут предложить высокий доход.",
    "Творчество:": "фокусируйтесь на креативных профессиях, таких как графический дизайнер или маркетолог.",
    "Стабильность:": "Работа в государственных учреждениях или крупных корпорациях может обеспечить большую стабильность.",
    "Программирование:": "Рассмотрите удаленные вакансии разработчика программного обеспечения.",
    "Дизайн:": "Командная работа в дизайнерской студии может быть отличным вариантом для вас.",
    "Наука:": "Карьерный путь аналити ка в научной области может быть вам интересен.",
    "Музыка:": "Вы можете рассмотреть работу в сфере медиапланирования или в музыкальной компании."
}



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассказать о себе")
    item2 = types.KeyboardButton("Рекомендации")
    item3 = types.KeyboardButton("Мои профессии")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '''Привет! Я советчик по карьере. 
Выбери действие:''', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Рассказать о себе")
def about_me(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Мои интересы")
    item2 = types.KeyboardButton("Мои навыки")
    item3 = types.KeyboardButton("Мое образование")
    item4 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Расскажи о себе:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Мои интересы")
def my_interes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить интересы")
    item2 = types.KeyboardButton("Посмотреть интересы")
    item3 = types.KeyboardButton("Удалить интересы")
    item4 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбери что ты хочешь сделать:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Добавить интересы")
def add_interest(message):
    bot.send_message(message.chat.id, "Введите ваш интерес:")
    bot.register_next_step_handler(message, inser_interesi)
def inser_interesi(message,):
    name = message.text
    manager.insert_interests([(name)])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Интерес сохранен", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Посмотреть интересы")
def viev_interes(message):
    user_id = message.from_user.id
    viev_in = manager.view_interests(user_id)
    if viev_in:
        text = "\n".join([f"Interest: {x[0]}" for x in viev_in])
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[0] for x in viev_in]))
    else:
        no_sach(message)

@bot.message_handler(func=lambda message: message.text == "Удалить интересы")
def delete_interes(message):
    user_id = message.from_user.id
    manager.delete_interest(user_id)
    bot.send_message(message.chat.id, "Интересы удалены")

@bot.message_handler(func=lambda message: message.text == "Мое образование")
def my_obr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить образование")
    item2 = types.KeyboardButton("Удалить образование")
    item3 = types.KeyboardButton("Посмотреть образование")
    item4 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбери что ты хочешь сделать:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Добавить образование")
def add_obr(message):
    bot.send_message(message.chat.id, "Введите ваше образование:")
    bot.register_next_step_handler(message, add_obrz)
def add_obrz(message):
    name = message.text
    manager.insert_obr([(name)])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Образование сохраненно", reply_markup=markup )


@bot.message_handler(func=lambda message: message.text == "Удалить образование")
def del_obr(message):
    bot.send_message(message.chat.id, "Введите образование для удаления:")
    user_id = message.from_user.id
    manager.view_education(user_id) 
    bot.register_next_step_handler(message, delete_obr, user_id)  
def delete_obr(message, user_id):
    name = message.text
    manager.delete_education(user_id, name)  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Образование удалено", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == "Посмотреть образование")
def viev_obrazovanie(message):
    user_id = message.from_user.id
    view_in = manager.view_education(user_id)
    if view_in:
        text = "\n".join([f"Образование: {x[0]}" for x in view_in])
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[0] for x in view_in]))
    else:
        no_sach(message)


@bot.message_handler(func=lambda message: message.text == "Мои навыки")
def my_skills(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить навыки")
    item2 = types.KeyboardButton("Удалить навыки")
    item3 = types.KeyboardButton("Посмотрть навыки")
    item4 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбери что ты хочешь сделать:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Добавить навыки")
def add_skills(message):
    bot.send_message(message.chat.id, "Введите ваш навык:")
    bot.register_next_step_handler(message, add_skils)
def add_skils(message):
    name = message.text
    manager.insert_skills([(name)])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Навык сохранён", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Удалить навыки")
def del_skill(message):
    user_id = message.from_user.id
    manager.delete_skill(user_id) 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Навыки удалены.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть навыки")
def viev_skills(message):
    user_id = message.from_user.id
    viev_in = manager.view_skills(user_id)
    if viev_in:
        text = "\n".join([f"Навыки: {x[0]}" for x in viev_in]) 
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[0] for x in viev_in]))
    else:
        no_sach(message)
        

@bot.message_handler(func=lambda message: message.text == "Рекомендации")
def recomendation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посмотреть рекомендации")
    item2 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выбери что ты хочешь сделать:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть рекомендации")
def viev_recomindation(message):
    faq_message = "Это наши рекомендации(мы вам покажем рекомендации по вашим навыкам и интересам(их вы можете посмотреть по /start):\n\n"
    for question, answer in RECOMENDATION.items():
        faq_message += f"*Ваш интерес:* {question}\n*Профессия:* {answer}\n\n"
    bot.send_message(message.chat.id, faq_message, parse_mode='Markdown')
    

@bot.message_handler(func=lambda message: message.text == "Мои профессии")
def my_interes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить профессию")
    item2 = types.KeyboardButton("Посмотреть профессии")
    item3 = types.KeyboardButton("Удалить профессии")
    item4 = types.KeyboardButton("Главное меню")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбери что ты хочешь сделать:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Добавить профессию")
def inser_professia(message):
    bot.send_message(message.chat.id, "Введите вашу профессию:")
    bot.register_next_step_handler(message, inser_profesia)
def inser_profesia(message):
        name = message.text
        manager.insert_job([(name)])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Главное меню")
        markup.add(item1)
        bot.send_message(message.chat.id, "Профессия сохранена", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть профессии")
def viev_professia(message):
    user_id = message.from_user.id
    viev_in = manager.view_current_job(user_id)
    if viev_in:
        text = "\n".join([f"Профессия: {x[0]}" for x in viev_in])
        bot.send_message(message.chat.id, text, reply_markup=gen_markup([x[0] for x in viev_in]))
    else:
        no_sach(message)


@bot.message_handler(func=lambda message: message.text == "Удалить профессии")
def delete_professia(message):
    user_id = message.from_user.id
    delete_interes = manager.insert_interests(user_id)
    if delete_interes:
        text = "\n".join([f"Project name:{x[0]} \nLink:{x[4]}\n" for x in delete_interes])
        delete_interes = [x[2] for x in delete_interes]
        bot.send_message(message.chat.id, text, reply_markup=gen_markup(delete_interes))
    else:
        no_sach(message)


@bot.message_handler(func=lambda message: message.text == "Главное меню")
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассказать о себе")
    item2 = types.KeyboardButton("Рекомендации")
    item3 = types.KeyboardButton("Мои профессии")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def default_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.reply_to(message, "Извини, я тебя не понял. Попробуй снова", reply_markup=markup)


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()