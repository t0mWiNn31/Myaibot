import telebot
import os
from groq import Groq

# Render ရဲ့ Environment Variables ထဲမှာ ထည့်ပေးရမယ့် Key တွေ
TOKEN = os.environ.get('BOT_TOKEN')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟိုင်း ကိုကို! Groq AI Bot အဆင်သင့်ပါပဲ။ ဘာကူညီရမလဲ?")

@bot.message_handler(func=lambda message: True)
def get_ai_response(message):
    try:
        # Groq API ဆီကနေ Llama 3 နဲ့ အဖြေတောင်းတာ
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": message.text}],
        )
        
        ai_reply = completion.choices[0].message.content
        bot.reply_to(message, ai_reply)
        
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.infinity_polling()
