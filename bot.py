import telebot
from flask import Flask, send_from_directory
import threading
import os

BOT_TOKEN = "YOUR_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)


@app.route('/user/<chat_id>')
def user_page(chat_id):
    return send_from_directory('.', 'index.html')


def run_bot():
    bot.infinity_polling()


threading.Thread(target=run_bot).start()


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
