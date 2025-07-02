import os
import django
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler
)
from decouple import config
from asgiref.sync import sync_to_async

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')
django.setup()

from core.models import TelegramUser
from core.tasks import send_welcome_email

TELEGRAM_TOKEN = config('TELEGRAM_BOT_TOKEN')
ASK_EMAIL = 1

@sync_to_async
def save_user(chat_id, username):
    return TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={'username': username}
    )

@sync_to_async
def update_email(chat_id, email):
    try:
        user = TelegramUser.objects.get(chat_id=chat_id)
        user.email = email
        user.save()
        return user.username
    except:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    username = update.effective_chat.username or "NoUsername"

    user, created = await save_user(chat_id, username)

    if created:
        await update.message.reply_text(f"Welcome, {username}! Please enter your email.")
        return ASK_EMAIL
    else:
        await update.message.reply_text(f"Hi again, {username}! You're already registered.")
        return ConversationHandler.END

async def receive_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    email = update.message.text.strip()

    if '@' not in email:
        await update.message.reply_text("⚠ Please enter a valid email address.")
        return ASK_EMAIL

    username = await update_email(chat_id, email)
    if username:
        send_welcome_email.delay(email)
        await update.message.reply_text(f"Hi {username}! You are now registered.")
    else:
        await update.message.reply_text("❌ Something went wrong. Try /start again.")

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_email)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv)
    print("Bot is polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
