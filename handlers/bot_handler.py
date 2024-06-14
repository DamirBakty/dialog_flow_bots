import logging


class BotHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id
        super().__init__()

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(self.chat_id, log_entry)


def get_bot_handler(bot, chat_id):
    bot_handler = BotHandler(bot, chat_id)
    bot_handler.setLevel(logging.ERROR)
    bot_handler.setFormatter(logging.Formatter('%(message)s'))
    return bot_handler
