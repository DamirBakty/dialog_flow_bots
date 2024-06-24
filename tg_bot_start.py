import logging

from environs import Env
from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from handlers.bot_handler import BotHandler
from handlers.dialog_flow_handler import detect_intent_texts

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    update.message.reply_markdown_v2(
        'Бот связанный с DialogFlow',
        reply_markup=ForceReply(selective=True),
    )


def reply_message(update: Update, context: CallbackContext) -> None:
    try:
        user = update.effective_user
        user_id = user.id
        user_message = update.message.text
        dialog_flow_project_id = context.bot_data.get('dialog_flow_project_id')
        path_to_credentials = context.bot_data.get('path_to_credentials')

        reply_message, is_fallback = detect_intent_texts(
            project_id=dialog_flow_project_id,
            session_id=user_id,
            text=user_message,
            path_to_credentials=path_to_credentials
        )

        update.message.reply_text(reply_message)

    except Exception as e:
        logger.exception(e)


def main() -> None:
    env = Env()
    env.read_env()
    tg_chat_id = env.str('TG_CHAT_ID')
    tg_bot_token = env.str('TG_BOT_TOKEN')
    dialog_flow_project_id = env.str('DIALOGFLOW_PROJECT_ID')
    path_to_credentials = env.str('PATH_TO_CREDENTIALS')

    tg_bot = Bot(token=tg_bot_token)
    bot_handler = BotHandler(tg_bot, tg_chat_id)
    logger.addHandler(bot_handler)

    updater = Updater(tg_bot_token)

    dispatcher = updater.dispatcher
    dispatcher.bot_data['dialog_flow_project_id'] = dialog_flow_project_id
    dispatcher.bot_data['path_to_credentials'] = path_to_credentials

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
