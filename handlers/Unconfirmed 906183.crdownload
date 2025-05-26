async def handle_social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📷 اینستاگرام":
        await update.message.reply_text("لینک صفحه اینستاگرام:\nhttps://www.instagram.com/heyvanakco/", reply_markup=social_media_keyboard())
    elif text == "💬 تلگرام":
        await update.message.reply_text("لینک کانال تلگرام:\nhttps://t.me/s/heyvanakads", reply_markup=social_media_keyboard())
    elif text == "▶️ یوتیوب":
        await update.message.reply_text("لینک کانال یوتیوب:\nhttps://www.youtube.com/channel/UCRMH30RD2OWrZ4jFzUGL3eA", reply_markup=social_media_keyboard())
    elif text == "🔙 بازگشت":
        await update.message.reply_text("بازگشت به منوی اصلی:", reply_markup=main_menu_keyboard())