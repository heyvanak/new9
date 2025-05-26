import feedparser
from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import ads_category_keyboard

async def handle_ads_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # آدرس RSS هر دسته
    rss_links = {
        "🐶 سگ‌ها": "https://heyvanak.com/ads/adopt-dog/feed",
        "🐱 گربه‌ها": "https://heyvanak.com/ads/adopt-cat/feed",
        "🐦 پرندگان": "https://heyvanak.com/ads/adopt-birds/feed",
        "🐹 جوندگان": "https://heyvanak.com/ads/adopt-rodents/feed",
        "🐠 آبزیان": "https://heyvanak.com/ads/adopt-fish/feed"
    }

    # بررسی اینکه آیا دسته انتخاب شده وجود دارد یا خیر
    if text in rss_links:
        # خواندن داده‌های RSS
        feed = feedparser.parse(rss_links[text])
        
        # استخراج ۱۰ آگهی اخیر
        ads = ""
        for entry in feed.entries[:10]:
            title = entry.title
            link = entry.link
            ads += f"{title}\n{link}\n\n"

        # ارسال آگهی‌ها به کاربر
        if ads:
            await update.message.reply_text(f"لیست آگهی‌های {text}:\n{ads}", reply_markup=ads_category_keyboard())
        else:
            await update.message.reply_text(f"هیچ آگهی جدیدی برای {text} وجود ندارد.", reply_markup=ads_category_keyboard())
    elif text == "🔙 بازگشت":
        await update.message.reply_text("بازگشت به منوی اصلی:", reply_markup=main_menu_keyboard())

from telegram.ext import MessageHandler, filters

# اضافه کردن هندلر
ads_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ads_category)
