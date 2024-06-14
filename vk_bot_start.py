import random

import vk_api as vk
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow_handler import detect_intent_texts


def echo(event, vk_api, message):
    vk_api.messages.send(
        user_id=event.user_id,
        message=message,
        random_id=random.randint(1, 1000)
    )


def main():
    env = Env()
    env.read_env()
    vk_bot_token = env.str('VK_BOT_TOKEN')
    dialog_flow_project_id = env.str('DIALOGFLOW_PROJECT_ID')
    path_to_credentials = env.str('PATH_CREDENTIALS')

    vk_session = vk.VkApi(token=vk_bot_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message = detect_intent_texts(
                project_id=dialog_flow_project_id,
                session_id=event.user_id,
                path_to_credentials=path_to_credentials,
                text=event.text
            )
            echo(event, vk_api, message)


if __name__ == '__main__':
    main()
