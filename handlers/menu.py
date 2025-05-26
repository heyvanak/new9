from telegram.ext import MessageHandler, filters
from telegram import Update
from utils.keyboards import main_menu_keyboard, ads_category_keyboard, social_media_keyboard
from telegram.ext import ContextTypes
async def handle_menu_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # دکمه‌های منوی اصلی
    if text == "📋 مشاهده آگهی‌ها":
        await update.message.reply_text("لطفاً یک دسته‌بندی را انتخاب کنید:", reply_markup=ads_category_keyboard())
    elif text == "📱 شبکه‌های اجتماعی":
        await update.message.reply_text("لطفاً یکی از شبکه‌های اجتماعی زیر را انتخاب کنید:", reply_markup=social_media_keyboard())
    elif text == "➕ ثبت آگهی":
        await update.message.reply_text("برای ثبت آگهی لطفاً وارد سایت شوید:\nhttps://heyvanak.com/newad", reply_markup=main_menu_keyboard())
    elif text == "🌐 مشاهده سایت":
        await update.message.reply_text("برای مشاهده سایت از لینک زیر استفاده کنید:\nhttps://heyvanak.com", reply_markup=main_menu_keyboard())
    elif text == "🔙 بازگشت":
        await update.message.reply_text("بازگشت به منوی اصلی:", reply_markup=main_menu_keyboard())
    else:
        await update.message.reply_text("گزینه نامعتبر. لطفاً از منوی زیر انتخاب کنید:", reply_markup=main_menu_keyboard())

menu_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_selection)
