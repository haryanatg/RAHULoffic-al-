import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8454755219:AAHNPR1emfIcrOfCWZCrHHsB-clvXb7j2kg")  # env var se token

if not TOKEN:
    raise RuntimeError("8454755219:AAHNPR1emfIcrOfCWZCrHHsB-clvXb7j2kg")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome To RAHUL OFFICIAL BOT 😄 \n\n"
        "Commands:\n"
        "/photo [url]  → photo bheje (agar url na do to local photo.jpg)\n"
        "/video [url]  → video bheje (agar url na do to local video.mp4)\n"
        "/text <msg>   → wahi text reply kare"
    )

# /photo (local file ya URL)
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        url = context.args[0]
        await update.message.reply_photo(url)
        return
    # local fallback
    path = "photo.jpg"
    try:
        with open(path, "rb") as f:
            await update.message.reply_photo(f)
    except FileNotFoundError:
        await update.message.reply_text("❗ 'photo.jpg' nahi mila. Use: /photo <image-url>")

# /video (local file ya URL)
async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        url = context.args[0]
        await update.message.reply_video(url)
        return
    # local fallback
    path = "video.mp4"
    try:
        with open(path, "rb") as f:
            await update.message.reply_video(f)
    except FileNotFoundError:
        await update.message.reply_text("❗ 'video.mp4' nahi mila. Use: /video <video-url>")

# /text <message>
async def text_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Use: /text aapka-message")
        return
    await update.message.reply_text(" ".join(context.args))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("photo", photo))
    app.add_handler(CommandHandler("video", video))
    app.add_handler(CommandHandler("text", text_cmd))
    app.run_polling(allowed_updates=Update.ALL_TYPES)  # simple & reliable

if __name__ == "__main__":
    main()
