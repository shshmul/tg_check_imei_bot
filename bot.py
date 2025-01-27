# bot.py
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
from services.imei_service import validate_imei, get_imei_info
from config import BOT_TOKEN, WHITELIST


# Логгирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        "Привет! Отправьте IMEI",
        reply_markup=ForceReply(selective=True)
    )


async def check_imei(update: Update, context: CallbackContext):
    user_id = str(update.message.from_user.id)
    # Проверка пользователя на доступ к базе
    if user_id not in WHITELIST:
        await update.message.reply_text("Недостаточно прав для доступа к этой функции")
        return

    imei = update.message.text.strip()
    # Проверка имей номер ли отправляется пользователем
    if not validate_imei(imei):
        await update.message.reply_text("Неверный IMEI")
        return

    imei_info = get_imei_info(imei)
    await update.message.reply_text(f"Информация о IMEI: {imei_info}")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    # dp = updater.dispatcher
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_imei))
    application.run_polling()

    # updater.start_polling()
    # updater.idle()
