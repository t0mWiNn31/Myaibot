import os
import telebot
import google.generativeai as genai

# Environment Variables ဆွဲယူခြင်း
TOKEN = os.environ.get('BOT_TOKEN')
API_KEY = os.environ.get('GEMINI_API_KEY')

# Gemini ကို ချိတ်ဆက်ခြင်း
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Telegram Bot ကို ချိတ်ဆက်ခြင်း
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # User ပို့လိုက်တဲ့ message ကို Gemini ဆီ ပို့မယ်
        response = model.generate_content(message.text)
        
        # အဖြေကို Telegram မှာ ပြန်ပြမယ်
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error logic: {e}")
        bot.reply_to(message, "Error တက်နေတယ် ကိုကို။")

if name == "main":
    bot.infinity_polling()
