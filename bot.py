import telebot
from flask import Flask, send_from_directory
import threading
import os

# ======================
BOT_TOKEN = "8520087047:AAEbINFxeI5dLH68ZEiSVxKvRH2-8Dvo8W8"
# ======================

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

HTML_FILE = "index.html"


# ======================
# Telegram Bot
# ======================
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    link = f"http://YOUR_RENDER_URL/user/{chat_id}"

    bot.send_message(chat_id, f"তোমার link:\n{link}")


# ======================
# Web Route
# ======================
@app.route('/user/<chat_id>')
def user_page(chat_id):
    return send_from_directory('.', HTML_FILE)


# ======================
# Run Bot
# ======================
def run_bot():
    bot.infinity_polling()


threading.Thread(target=run_bot).start()


# ======================
# Render PORT FIX
# ======================
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
