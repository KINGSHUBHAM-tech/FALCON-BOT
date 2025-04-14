from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "7739852361:AAFwsEaiqBayd8eDH3Vnza6Izu4vwdN9Gi0"
KEYWORDS = ["deal", "dm", "price", "bundle", "coin"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if any(word in text for word in KEYWORDS):
            try:
                await update.message.delete()
            except:
                pass

            await update.message.reply_text(
                f"Hey [{update.effective_user.first_name}](tg://user?id={update.effective_user.id}), "
                "your message was removed due to banned words.",
                parse_mode="Markdown"
            )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_message))
app.run_polling()
