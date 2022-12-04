from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

bot = Bot (token= '5832572496:AAHE8OuYUBTpJe-YopbZXwtzgpaS0BEZ0nE')
updater = Updater (token= '5832572496:AAHE8OuYUBTpJe-YopbZXwtzgpaS0BEZ0nE')
dispatcher = updater.dispatcher

def start (update, context) :
    text = update. message.text.split ()
    lst = []
    for i in text:
        if 'абв' not in i:
            lst.append (i)
    context.bot. send_message (update.effective_chat.id,list)



start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)



updater.start_polling ()
updater.idle()



