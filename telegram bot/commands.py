from telegram import Update, Bot, _bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater, filters,MessageHandler, CallbackContext, ConversationHandler
import datetime
import dictionary

# Commands

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/help\n/time\n')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


# Reactions
async def voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{update.effective_user.first_name}, давай без голосовых, я их не понимаю')

async def echo(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def delete_abv (update, context):
    text = update.message.text.split()
    list = []
    for i in text: 
        if 'абв'not in text:
            list.append(i)
            
    await context.bot.send_message(list)
   #await context.bot.send_message(chat_id=update.effective_chat.id, list),
    
    
    
        
#context.bot. send_message (update.effective_chat.id, ' ' join(list))




#Conversation

A = 0
B = 1

async def first_hello (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{update.effective_user.first_name}, привет! Как дела?')
    return A

async def HowAreYou (update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if dictionary.How_are_you_good_replies in text.lower():
        await update.message.reply_text(f'Это здорово! Как погода?')
    if dictionary.How_are_you_negative in text.lower():
        await update.message.reply_text(f'Не печалься, все будет ок! Как погода?')
    else:
        await update.message.reply_text(f'Все норм! Как погода кстати?')
    return B

async def Weather (update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if dictionary.How_are_you_good_replies in text.lower():
        await update.message.reply_text(f'Великолепно! У нас ботов правда нет погоды(')
    if dictionary.How_are_you_negative in text.lower():
        await update.message.reply_text(f'Не так уж и плохо. Подумай каково')
    else:
        await update.message.reply_text(f'Все норм! Как погода кстати?')
    return ConversationHandler.END

async def conv_end (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Ну все, пока')
    
async def First_Conv (update: Update, context: ContextTypes.DEFAULT_TYPE):
    conv = ConversationHandler(entry_points = [first_hello],
                        states = {A: [HowAreYou],
                                  B: [Weather]},
                                  fallbacks = [conv_end])
    await update.message.reply_text(f'Ну все, пока')






# async def square(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     print(msg)
    # lst = msg.split()
    # x = int(lst[1])
    # y = int(lst[2])
    # update.message.reply_text (f'{x} + {y} = {x+y}')
