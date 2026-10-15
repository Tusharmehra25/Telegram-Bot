import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# List of allowed user IDs (replace with actual IDs)
ALLOWED_USERS = [123456789]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Use /getlink to request your invite link.')

async def get_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    try:
        # Replace with your channel ID
        invite_link = await context.bot.create_chat_invite_link(
            chat_id='YOUR_CHANNEL_ID',
            member_limit=1
        )
        await update.message.reply_text(f"Here is your invite link: {invite_link.invite_link}")
    except Exception as e:
        await update.message.reply_text("Failed to create invite link. Make sure I am an admin in the channel.")
        logging.error(f"Error creating link: {e}")

if __name__ == '__main__':
    TOKEN = 'YOUR_BOT_TOKEN'
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('getlink', get_link))
    
    application.run_polling()
