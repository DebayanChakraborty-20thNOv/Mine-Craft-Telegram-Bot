from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5187936057:AAGYBE2byavRmZNhJbLDV_zRzLsh4GuQAFg",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hey there, I am Minecraft Bot. Welcome here!!. Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/getMinecraft - To download the official Minecraft Education Edition Game
	/getMinecraftID - To get Minecraft ID
	/learnMinecraft - To learn Minecraft free of cost
	/minecraftContest - To participate in the Minecraft Contest""")


def getMinecraftID_url(update: Update, context: CallbackContext):
	update.message.reply_text("Get your Minecraft ID =>\
	https://www.youtube.com/watch?v=Kkw-Z0D5Ydc&list=PLeVoANZdfMVRBU8YHYHboxlhkhyPFy5ch&index=1")


def getMinecraft_url(update: Update, context: CallbackContext):
	update.message.reply_text("Download Minecraft Link =>\
	https://education.minecraft.net/en-us/get-started/download")


def learnMinecraft_url(update: Update, context: CallbackContext):
	update.message.reply_text("Learn Minecraft with Anurag => \
		https://www.youtube.com/watch?v=RvpbzJNNTt0&list=PLeVoANZdfMVRBU8YHYHboxlhkhyPFy5ch&index=4")


def minecraftContest_url(update: Update, context: CallbackContext):
	update.message.reply_text("Download Minecraft Link =>\
	https://sites.google.com/view/smartgurucool/home")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('getMinecraft', getMinecraft_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('learnMinecraft', learnMinecraft_url))
updater.dispatcher.add_handler(CommandHandler('getMinecraftID', getMinecraftID_url))
updater.dispatcher.add_handler(CommandHandler('minecraftContest', minecraftContest_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
