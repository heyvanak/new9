import os
from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.menu import menu_handler
from handlers.ads import ads_handler
from config import BOT_TOKEN

# آدرس دامنه اپلیکیشن در Render (با HTTPS)
APP_URL = os.environ.get("APP_URL", "https://your-app-name.onrender.com") + f"/{BOT_TOKEN}"

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ثبت هندلرها
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(ads_handler)

    # ست کردن webhook و اجرای وب‌سرور
    await app.bot.set_webhook(APP_URL)
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 443)),
        webhook_url=APP_URL
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
