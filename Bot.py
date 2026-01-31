import os
import telebot
import google.generativeai as genai

# Render ရဲ့ Environment Variables ထဲကနေ Key တွေကို ဆွဲယူမယ်
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# Gemini API ကို Setup လုပ်ခြင်း
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        # AI ကို မြန်မာလို ပိုပီပြင်အောင် ညွှန်ကြားချက် ထည့်ထားပါတယ်
        prompt = f"You are a helpful assistant. Please reply in natural, colloquial Myanmar language (Burmese). Be friendly and avoid robotic sounding formal words. Question: {message.text}"
        
        response = model.generate_content(prompt)
        
        # စာပြန်တဲ့နေရာမှာ စာသားပါရင် ပြန်မယ်
        if response.text:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "နားမလည်လို့ပါ ကိုကို။ နောက်တစ်ခါ ပြန်ပြောပေးမလား?")
            
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "ခဏလေးနော် ကိုကို... Gemini Key ဒါမှမဟုတ် Network ကြောင့် Error တက်သွားလို့ပါ။")

if name == "main":
    bot.infinity_polling()
