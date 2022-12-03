from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater,MessageHandler, filters, ConversationHandler
import commands
import dictionary
import datetime


app = ApplicationBuilder().token("5832572496:AAHE8OuYUBTpJe-YopbZXwtzgpaS0BEZ0nE").build()

#commands
app.add_handler(CommandHandler("help", commands.help))
app.add_handler(CommandHandler("time", commands.time))
#reactions
app.add_handler(MessageHandler(filters.VOICE, commands.voice))
app.add_handler(MessageHandler(filters.Text, commands.delete_abv))


#conversations
# app.add_handler(ConversationHandler(entry_points = [commands.first_hello],
#     states = {commands.A: [commands.HowAreYou],
#               commands.B: [commands.Weather]},
#     fallbacks = [commands.conv_end]))


# app.add_handler(MessageHandler(filters.Text, commands.echo))

 
print('success')
app.run_polling()



# app.add_handler(MessageHandler(filters.Text(dictionary.hello_messages),commands.text_reply))