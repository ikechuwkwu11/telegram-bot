from flask import Flask,request
from sqlalchemy.event import dispatcher
from telegram import Bot,Update
from telegram.ext import CommandHandler,MessageHandler,filters,CallbackContext,Application


TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
WEBHOOK_URL = "https://your-domain.com/webhook"

app = Flask(__name__)
bot = Bot(token=TOKEN)
application =Application.builder().token(TOKEN).build()

def start(update:Update, context:CallbackContext):
    update.message.reply_text("Hello I a bot and i am here to help you.")

def echo(update: Update, context:CallbackContext):
    update.message.reply_text(update.message.text)


application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(),bot)
    dispatcher.process_update(update)
    return "OK",200

@app.route('/')
def home():
    return "Bot is running!"


if __name__ == '__main__':
    app.run(debug=True)

