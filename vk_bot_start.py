import logging
import random

import vk_api as vk
from environs import Env
from telegram import Bot
from vk_api.longpoll import VkLongPoll, VkEventType

from handlers.bot_handler import BotHandler
from handlers.dialog_flow_handler import detect_intent_texts

logger = logging.getLogger()


def reply_message(event, vk_api, message):
    vk_api.messages.send(
        user_id=event.user_id,
        message=message,
        random_id=random.randint(1, 1000)
    )


def main():
    env = Env()
    env.read_env()
    tg_chat_id = env.str('TG_CHAT_ID')
    tg_bot_token = env.str('TG_BOT_TOKEN')
    vk_bot_token = env.str('VK_BOT_TOKEN')
    dialog_flow_project_id = env.str('DIALOGFLOW_PROJECT_ID')
    path_to_credentials = env.str('PATH_TO_CREDENTIALS')

    tg_bot = Bot(token=tg_bot_token)
    bot_handler = BotHandler(tg_bot, tg_chat_id)
    logger.addHandler(bot_handler)

    vk_session = vk.VkApi(token=vk_bot_token)
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)

    for event in long_poll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message, is_fallback = detect_intent_texts(
                    project_id=dialog_flow_project_id,
                    session_id=event.user_id,
                    path_to_credentials=path_to_credentials,
                    text=event.text
                )
                if not is_fallback:
                    reply_message(event, vk_api, message)
        except Exception as e:
            logger.exception(e)


if __name__ == '__main__':
    main()
