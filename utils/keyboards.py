from telegram import ReplyKeyboardMarkup

# منوی اصلی
def main_menu_keyboard():
    keyboard = [
        ["➕ ثبت آگهی", "📋 مشاهده آگهی‌ها"],
        ["🌐 مشاهده سایت", "📱 شبکه‌های اجتماعی"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# منوی دسته‌بندی آگهی‌ها
def ads_category_keyboard():
    keyboard = [
        ["🐶 سگ‌ها", "🐱 گربه‌ها"],
        ["🐦 پرندگان", "🐹 جوندگان"],
        ["🐠 آبزیان", "🔙 بازگشت"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# منوی شبکه‌های اجتماعی
def social_media_keyboard():
    keyboard = [
        ["📷 اینستاگرام", "💬 تلگرام"],
        ["▶️ یوتیوب", "🔙 بازگشت"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
