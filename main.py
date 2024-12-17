import telebot
from telebot import types
from config import *
from logic_bot import DB_Manager
import telebot.types 
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot(TOKEN)
cancel_button = "Отмена"


def cansel(message):
    bot.send_message(message.chat.id, "Главное меню")

def gen_inline_markup(rows):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for row in rows:
        markup.add(InlineKeyboardButton(row, callback_data=row))
    return markup

def gen_markup(rows):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 1
    for row in rows:
        markup.add(KeyboardButton(row))
    markup.add(KeyboardButton(cancel_button))
    return markup


def no_sach(message):
    bot.send_message(message.chat.id, 'Ничего не найдено. Список пуст')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассказать о себе")
    item2 = types.KeyboardButton("Рекомендации")
    markup.add(item1, item2)
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
def inser_interes(message):
    bot.send_message(message.chat.id, "Введите ваш интерес:")
    bot.register_next_step_handler(message, inser_interesi)
def inser_interesi(message):
        name = message.text
        manager.insert_interesti([(name)])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Главное меню")
        markup.add(item1)
        bot.send_message(message.chat.id, "Интерес сохранен", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть интересы")
def viev_interes(message):
    user_id = message.from_user.id
    viev_in = manager.viev_int(user_id)
    if viev_in:
        text = "\n".join([f"Project name:{x[2]}" for x in viev_in])
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[2] for x in viev_in]))
    else:
        no_sach(message)

        
        

@bot.message_handler(func=lambda message: message.text == "Удалить интересы")
def delete_interes(message):
    user_id = message.from_user.id
    delete_interes = manager.insert_interests(user_id)
    if delete_interes:
        text = "\n".join([f"Project name:{x[2]} \nLink:{x[4]}\n" for x in delete_interes])
        delete_interes = [x[2] for x in delete_interes]
        bot.send_message(message.chat.id, text, reply_markup=gen_markup(delete_interes))
    else:
        no_sach(message)


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
def delete_obr(message):
    user_id = message.from_user.id
    projects = manager.get_projects(user_id)
    if projects:
        text = "\n".join([f"Project name:{x[2]} \nLink:{x[4]}\n" for x in projects])
        projects = [x[2] for x in projects]
        bot.send_message(message.chat.id, text, reply_markup=gen_markup(projects))
    else:
        no_sach(message)


@bot.message_handler(func=lambda message: message.text == "Посмотреть образование")
def viev_obr(message):
    user_id = message.from_user.id
    viev_in = manager.viev_int(user_id)
    if viev_in:
        text = "\n".join([f"Project name:{x[2]}" for x in viev_in])
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[2] for x in viev_in]))
    else:
        no_sach(message)
        


@bot.message_handler(func=lambda message: message.text == "Мои навыки")
def my_skills(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить навыки")
    item2 = types.KeyboardButton("Удалить навыки")
    item3 = types.KeyboardButton("Посмотерть навыки")
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
    manager.del_skills([(user_id)])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Навыки удалёны", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть навыки")
def viev_skills(message, c):
    user_id = message.from_user.id
    viev_in = manager.viev_int(user_id)
    if viev_in:
        text = '\n\n'.join([', '.join(map(str, x)) for x in c])
        bot.send_message(message.from_user.id, text)
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
    user_id = message.from_user.id
    projects = manager.viev_rec(user_id)

    
@bot.message_handler(func=lambda message: message.text == "Главное меню")
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассказать о себе")
    item2 = types.KeyboardButton("Рекомендации")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Привет! Я советчик по карьере. Выбери действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def default_message(message):
    bot.reply_to(message, "Извини, я тебя не понял. Попробуй снова")


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()