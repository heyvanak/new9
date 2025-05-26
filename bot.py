from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from config import BOT_TOKEN
from handlers.menu import menu_handler


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(start_handler)
app.add_handler(menu_handler)

app.run_polling()
