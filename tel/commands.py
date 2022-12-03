from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import logging

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.log(update,context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/help\n/time\n/square\n')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def square(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    # lst = msg.split()
    # x = int(lst[1])
    # y = int(lst[2])
    # update.message.reply_text (f'{x} + {y} = {x+y}')


