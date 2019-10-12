from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from weather import get_forecast

updater=Updater(token="678181659:AAE3S1DwMIy3NttdXX1BZ1AEkc34SLLbkSE")

#allows to register handler -> command,text,video,audio,etc
dispatcher=updater.dispatcher

#define a callback funtion
def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, Welcome to RIshiWeaterBot...")


# create a command handler
start_handler= CommandHandler("start",start)

# add command handler to dispatcher
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())

# create a text message handler
echo_handler=MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)

def option(bot,update):
    button=[
        [InlineKeyboardButton("Option 1",callback_data="1"),
        InlineKeyboardButton("Option 2", callback_data="2")],
        [InlineKeyboardButton("Option 3", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id,
                    text="Choose one option..",
                    reply_markup=reply_markup)

option_handler = CommandHandler("option",option)

dispatcher.add_handler(option_handler)

def button(bot,update):
    query=update.callback_query
    #firstly usded send_message for multiple messages now using edit message
    bot.edit_message_text(chat_id=query.message.chat_id,
                      text="Thanks for choosing {}.".format(query.data),
                      message_id=query.message.message_id
                      )

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

def get_location(bot,update):
    button=[
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup= ReplyKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id,
                    text="Mind sharing location..",
                    reply_markup=reply_markup)

get_location_handler= CommandHandler("location",get_location)
dispatcher.add_handler(get_location_handler)

def location(bot,update):
    lat=update.message.location.latitude
    lon=update.message.location.longitude
    forecasts=get_forecast(lat,lon)
    bot.send_message(chat_id=update.message.chat_id,
                    #text="Longitude : {} Latitude : {}".format(lon,lat),
                    text=forecasts,
                    reply_markup=ReplyKeyboardRemove())

location_handler= MessageHandler(Filters.location,location)
dispatcher.add_handler(location_handler)

#start polling
updater.start_polling()
