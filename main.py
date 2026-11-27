import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Cineinfo Bot 🎬\n\nKisi bhi movie ka naam bhejo:\n/movie Avengers")

async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Movie ka naam likho:\n/movie Avengers")
        return
    name = " ".join(context.args)
    await update.message.reply_text(f"🔍 Searching: {name}...")

if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("movie", movie))
    print("Bot chal raha hai...")
    app.run_polling()
