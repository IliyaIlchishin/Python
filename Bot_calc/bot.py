from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler 

bot = Bot (token= '5832572496:AAHE8OuYUBTpJe-YopbZXwtzgpaS0BEZ0nE')
updater = Updater (token= '5832572496:AAHE8OuYUBTpJe-YopbZXwtzgpaS0BEZ0nE')
dispatcher = updater.dispatcher



def parse (s):
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol 
        else:
            result.append(int (digit))
            digit = ""
            result.append (symbol)
    else:
        # if digit: 
        result.append(int (digit))
    return result
   
def calculate(lst):
    result = 0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index-1] / lst[index+1]
        lst= lst[:index-1] +[result]+lst[index+2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index-1] + lst[index+1]
        lst = lst[:index-1] + [result]+lst[index+2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index-1]- lst[index+1]
        lst = lst[:index-1] + [result]+lst[index+2:]
    return round(result,2)

def Start(update, context):
    context.bot.send_message(update.effective_chat.id, "Я бот-калькулятор, вводите числа и символы через пробел")
    data = update.message.text
    update.message.reply_text(f'ввели:{data}')
    lst = parse(data)
    result = calculate(lst)
    update.message.reply_text(f'Результат:{result}')
   


start_handler =CommandHandler('start', Start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()