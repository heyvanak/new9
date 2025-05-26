import os
import asyncio
import nest_asyncio
from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.menu import menu_handler
from handlers.ads import ads_handler
from config import BOT_TOKEN

# آدرس دامنه اپلیکیشن در Render (مثلاً: https://heyvanakbot.onrender.com)
APP_URL = os.environ.get("APP_URL", "https://new9-23.onrender.com") + f"/{BOT_TOKEN}"

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ثبت هندلرها
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(ads_handler)

    # ست کردن Webhook
    await app.bot.set_webhook(APP_URL)

    # اجرای وب‌سرور
    await app.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 443)),
        webhook_url=APP_URL
    )

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
