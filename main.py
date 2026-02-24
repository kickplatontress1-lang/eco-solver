import telebot
import os
    
bot = telebot.TeleBot("Здесь поменяйте это поле на свой токен (храните токен как пароль!!!)")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Этот бот предназначен для экономии пластика и сортировок отходов. /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Команды: \n /ideas - идеи для поделок из пластиковых бутылок. \n /sort - как нужно сортировать отходы. \n /degradation - разложение отходов")

@bot.message_handler(commands=['ideas'])
def send_ideas(message):
    with open('images/ideas.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
    bot.reply_to(message, "Идеи включают органайзеры для мелочей, садовые кашпо, автоматические системы полива, метлы, совки, детские игрушки, кормушки для птиц и даже элементы мебели, создавая функциональные предметы без затрат.")

@bot.message_handler(commands=['sort'])
def send_sort(message):
    with open('images/sort.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
    bot.reply_to(message, "Сортировки отходов в России: \n Синий - пластик, \n Красный - металл, \n Зелёный - бумага, \n Жёлтый - стекло.")

@bot.message_handler(commands=['degradation'])
def send_degradation(message):
    bot.reply_to(message, "Основными долгоживущими отходами являются: \n Пластиковые бутылки (450–1000 лет), \n  Стекло (1000+ лет), \n  Алюминиевые банки (100–200 лет), \n Автомобильные шины (более 100 лет).")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
