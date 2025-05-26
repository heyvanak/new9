from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from utils.keyboards import main_menu_keyboard, ads_category_keyboard, social_media_keyboard
import feedparser

async def handle_menu_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # منوی اصلی
    if text == "📋 مشاهده آگهی‌ها":
        await update.message.reply_text("لطفاً یک دسته‌بندی را انتخاب کنید:", reply_markup=ads_category_keyboard())

    elif text == "📱 شبکه‌های اجتماعی":
        await update.message.reply_text("لطفاً یکی از شبکه‌های اجتماعی زیر را انتخاب کنید:", reply_markup=social_media_keyboard())

    elif text == "➕ ثبت آگهی":
        await update.message.reply_text("برای ثبت آگهی لطفاً وارد سایت شوید:\nhttps://heyvanak.com/newad", reply_markup=main_menu_keyboard())

    elif text == "🌐 مشاهده سایت":
        await update.message.reply_text("برای مشاهده سایت از لینک زیر استفاده کنید:\nhttps://heyvanak.com", reply_markup=main_menu_keyboard())

    # بازگشت
    elif text == "🔙 بازگشت":
        await update.message.reply_text("بازگشت به منوی اصلی:", reply_markup=main_menu_keyboard())

    # دسته‌بندی آگهی‌ها
    elif text in ["🐶 سگ‌ها", "🐱 گربه‌ها", "🐦 پرندگان", "🐹 جوندگان", "🐠 آبزیان"]:
        rss_links = {
            "🐶 سگ‌ها": "https://heyvanak.com/ads/adopt-dog/feed",
            "🐱 گربه‌ها": "https://heyvanak.com/ads/adopt-cat/feed",
            "🐦 پرندگان": "https://heyvanak.com/ads/adopt-birds/feed",
            "🐹 جوندگان": "https://heyvanak.com/ads/adopt-rodents/feed",
            "🐠 آبزیان": "https://heyvanak.com/ads/adopt-fish/feed"
        }
        feed = feedparser.parse(rss_links[text])
        ads = ""
        for entry in feed.entries[:10]:
            title = entry.title
            link = entry.link
            ads += f"<b>{title}</b>\nبرای مشاهده آگهی روی این متن <a href='{link}'>اینجا کلیک کنید</a>\n\n"
        if ads:
            await update.message.reply_text(f"لیست آگهی‌های {text}:\n{ads}", reply_markup=ads_category_keyboard(), parse_mode='HTML')
        else:
            await update.message.reply_text(f"هیچ آگهی جدیدی برای {text} وجود ندارد.", reply_markup=ads_category_keyboard())

    # شبکه‌های اجتماعی
    elif text == "📷 اینستاگرام":
        await update.message.reply_text("لینک صفحه اینستاگرام:\nhttps://www.instagram.com/heyvanakco/", reply_markup=social_media_keyboard())

    elif text == "💬 تلگرام":
        await update.message.reply_text("لینک کانال تلگرام:\nhttps://t.me/s/heyvanakads", reply_markup=social_media_keyboard())

    elif text == "▶️ یوتیوب":
        await update.message.reply_text("لینک کانال یوتیوب:\nhttps://www.youtube.com/channel/UCRMH30RD2OWrZ4jFzUGL3eA", reply_markup=social_media_keyboard())

    # سایر موارد
    else:
        await update.message.reply_text("گزینه نامعتبر. لطفاً از منوی زیر انتخاب کنید:", reply_markup=main_menu_keyboard())

# فقط یک هندلر برای همه دکمه‌ها
menu_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_selection)
