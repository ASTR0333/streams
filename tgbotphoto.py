from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = 'Введите токен из @BotFather'
TARGET_USER_ID = 000000 #введите user id(отправьте сообщение в бот и введите туда то значение, которое будет выведено в терминал


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Отправь фото.')


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    print(f"User ID: {user_id}")

    if update.message.photo:
        file_id = update.message.photo[-1].file_id
    elif update.message.document:
        file_id = update.message.document.file_id
    else:
        await update.message.reply_text("Пожалуйста, отправьте фото или файл.")
        return

    await context.bot.send_message(chat_id=TARGET_USER_ID, text="Вот что вам отправили:")
    if update.message.photo:
        await context.bot.send_photo(chat_id=TARGET_USER_ID, photo=file_id)
    else:
        await context.bot.send_document(chat_id=TARGET_USER_ID, document=file_id)


application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.PHOTO | filters.Document.ALL, handle_photo))
application.run_polling()

