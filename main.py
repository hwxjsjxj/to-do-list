from telebot  import TeleBot
from config import TOKEN
import query

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text=f'Привет, {message.from_user.username}. Я бот - todolist, вот список команд:\n'
                     f'/add - добавить задачу\n'
                     f'/view - посмотреть задачи\n'
                     f'/remove - удалить задачу\n'
                     f'/change - изменить задачу\n')
    
@bot.message_handler(commands=['add'])
def get_task(message):
    bot.send_message(message.chat.id, text=f'напишите задачу ')
    bot.register_next_step_handler(message, add_task)

def add_task(message):
    user_id = message.from_user.id
    text = message.text

    bot.send_message(message.chat.id,text=query.add_task(user_id, text))


@bot.message_handler(commands=['view'])
def view_tasks(message):
    user_id = message.from_user.id
    if query.view_task(user_id):
        bot.send_message(message.chat.id,text=query.view_task(user_id))
    else:
        bot.send_message(message.chat.id,text=f'Задач нет')

@bot.message_handler(commands=['remove'])
def get_task_id(message):
    bot.send_message(message.chat.id, text=f'Напишите id задачи')
    bot.register_next_step_handler(message, remove_message)

def remove_message(message):
    user_id = message.from_user.id
    task_id = message.text

    bot.send_message(message.chat.id,text=query.remove_task(user_id, task_id))

@bot.message_handler(commands=['change'])
def get_task_id(message):
    bot.send_message(message.chat.id, text=f'напишите id задачи')
    bot.register_next_step_handler(message,get_new_text)

def get_new_text(message):
    task_id = message.text
    bot.send_message(message.chat.id, text=f'напишите новую задачу')
    bot.register_next_step_handler(message,change_message,task_id)

def change_message(message, task_id):
    user_id = message.from_user.id
    new_text = message.text
    
    bot.send_message(message.chat.id,text=query.change_task(user_id, task_id,new_text))
    

bot.polling(none_stop=True)