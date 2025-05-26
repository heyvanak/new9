from telegram import Update
async def handle_ads_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🐶 سگ‌ها":
        await update.message.reply_text("لیست آگهی‌های سگ‌ها:\nhttps://heyvanak.com/ads/adopt-dog/feed", reply_markup=ads_category_keyboard())
    elif text == "🐱 گربه‌ها":
        await update.message.reply_text("لیست آگهی‌های گربه‌ها:\nhttps://heyvanak.com/ads/adopt-cat/feed", reply_markup=ads_category_keyboard())
    elif text == "🐦 پرندگان":
        await update.message.reply_text("لیست آگهی‌های پرندگان:\nhttps://heyvanak.com/ads/adopt-birds/feed", reply_markup=ads_category_keyboard())
    elif text == "🐹 جوندگان":
        await update.message.reply_text("لیست آگهی‌های جوندگان:\nhttps://heyvanak.com/ads/adopt-rodents/feed", reply_markup=ads_category_keyboard())
    elif text == "🐠 آبزیان":
        await update.message.reply_text("لیست آگهی‌های آبزیان:\nhttps://heyvanak.com/ads/adopt-fish/feed", reply_markup=ads_category_keyboard())
    elif text == "🔙 بازگشت":
        await update.message.reply_text("بازگشت به منوی اصلی:", reply_markup=main_menu_keyboard())

from telegram.ext import MessageHandler, filters

ads_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ads_category)
