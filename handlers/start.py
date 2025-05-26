from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.keyboards import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name or "کاربر"
    text = f"سلام {user_first_name} 👋\nبه ربات حیوانک خوش اومدی!\n\nبرای شروع یکی از گزینه‌های زیر رو انتخاب کن:"
    await update.message.reply_text(text, reply_markup=main_menu_keyboard())

start_handler = CommandHandler("start", start)
