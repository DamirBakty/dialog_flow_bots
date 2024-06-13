import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog_flow_handler import detect_intent_texts

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


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    user_id = user.id
    user_message = update.message.text
    dialog_flow_project_id = context.bot_data.get('dialog_flow_project_id')
    path_to_credentials = context.bot_data.get('path_to_credentials')

    reply_message = detect_intent_texts(
        project_id=dialog_flow_project_id,
        session_id=user_id,
        text=user_message,
        path_to_credentials=path_to_credentials
    )

    update.message.reply_text(reply_message)


def main() -> None:
    env = Env()
    env.read_env()
    bot_token = env.str('BOT_TOKEN')
    dialog_flow_project_id = env.str('DIALOGFLOW_PROJECT_ID')
    path_to_credentials = env.str('PATH_CREDENTIALS')
    updater = Updater(bot_token)

    dispatcher = updater.dispatcher
    dispatcher.bot_data['dialog_flow_project_id'] = dialog_flow_project_id
    dispatcher.bot_data['path_to_credentials'] = path_to_credentials

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
