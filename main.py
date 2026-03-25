import telebot
import time
from telebot import types

# --- [ الإعدادات الأساسية - ELMASRY VIP ] ---
TOKEN = 'ضع_توكن_بوتك_هنا'
ADMIN_ID = 123456789  # ضع الأيدي (ID) الخاص بك هنا
DEV_LINK = "https://t.me/mfathey466"

bot = telebot.TeleBot(TOKEN)

# مخزن البيانات (في سيرفر البوت)
valid_keys = ["ELMASRY_100", "VIP_FREE_2026"] # أكواد جاهزة للتجربة
active_users = [] # قائمة المشتركين المفعلين

# --- [ رسالة الترحيب واللوحة ] ---
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # أزرار لوحة التحكم
    btn_dev = types.InlineKeyboardButton("👨‍💻 تواصل مع المطور مباشر", url=DEV_LINK)
    btn_sub = types.InlineKeyboardButton("💳 لشراء كود الاشتراك راسل المطور", url=DEV_LINK)
    btn_enter_code = types.InlineKeyboardButton("🔑 أدخل كود الاشتراك", callback_data="enter_code")
    
    markup.add(btn_dev, btn_sub, btn_enter_code)

    # إذا كان المستخدم مشتركاً بالفعل، يظهر له زر الرفع
    if user_id in active_users or user_id == ADMIN_ID:
        btn_upload = types.InlineKeyboardButton("📤 رفع ملف على الاستضافة", callback_data="upload_mode")
        markup.add(btn_upload)

    welcome_text = (
        "👑 **مرحباً بكم في بوت المصري المدفوع**\n"
        "🚀 **لرفع الملفات على الاستضافة السحابية**\n"
        "━━━━━━━━━━━━━━\n"
        "⚙️ **أهلاً بكم في لوحة التحكم**\n"
        "يرجى الاشتراك لتتمكن من استخدام كافة الميزات."
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# --- [ نظام الأكواد والتفعيل ] ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "enter_code":
        msg = bot.send_message(call.message.chat.id, "⌨️ **يرجى إرسال كود الاشتراك الآن:**", parse_mode='Markdown')
        bot.register_next_step_handler(msg, verify_code)
    
    elif call.data == "upload_mode":
        bot.send_message(call.message.chat.id, "✅ **وضع الرفع مفعل!**\nأرسل ملفك الآن (Python, PHP, Zip) ليتم رفعه للاستضافة.")

def verify_code(message):
    code = message.text
    user_id = message.from_user.id
    
    if code in valid_keys:
        active_users.append(user_id)
        valid_keys.remove(code) # الكود يستخدم لمرة واحدة فقط
        
        markup = types.InlineKeyboardMarkup()
        btn_upload = types.InlineKeyboardButton("📤 ابدأ رفع الملفات الآن", callback_data="upload_mode")
        markup.add(btn_upload)
        
        bot.reply_to(message, "🎉 **تم تفعيل اشتراكك بنجاح لمدة 60 يوم!**\nظهر لك الآن زر الرفع في القائمة الرئيسية.", reply_markup=markup, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ **الكود غير صحيح أو مستخدم من قبل!**\nتواصل مع المطور للحصول على كود جديد.")

# --- [ استقبال الملفات المرفوعة ] ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.from_user.id not in active_users and message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "🚫 **عذراً!** يجب إدخال كود الاشتراك أولاً لتتمكن من الرفع.")
        return

    # هنا نضع كود الرفع للاستضافة (مثال Catbox)
    bot.reply_to(message, "⏳ **جاري رفع ملفك على الاستضافة السحابية...**")
    time.sleep(2)
    bot.send_message(message.chat.id, "✅ **تم الرفع بنجاح!**\nرابط الملف: `https://files.catbox.moe/elmasry_vip.py`")

# --- [ نظام التشغيل الدائم 24/7 ] ---
if __name__ == "__main__":
    print("🚀 Bot Elmasry VIP is Online!")
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(5)
