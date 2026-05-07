import telebot
from flask import Flask, send_file
import threading
import os

# ======================
BOT_TOKEN = "8520087047:AAEbINFxeI5dLH68ZEiSVxKvRH2-8Dvo8W8"
# ======================

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

users = {}

HTML_FILE = "index.html"


# /start command
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = str(message.chat.id)

    users[chat_id] = True

    link = f"http://YOUR_RENDER_URL/user/{chat_id}"

    bot.send_message(chat_id, f"তোমার link:\n{link}")


# serve HTML page
@app.route('/user/<chat_id>')
def user_page(chat_id):
    if chat_id in users:
        return send_file(HTML_FILE)
    return "Invalid user"


# run bot
def run_bot():
    bot.infinity_polling()


threading.Thread(target=run_bot).start()


# PORT fix for Render
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)