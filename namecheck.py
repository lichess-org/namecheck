from typing import Any, Dict
from zulip_bots.lib import BotHandler

from config import username_stream, zuliprc
from similar import find_most_similar_already_discussed


class NameCheckHandler:
    def usage(self) -> str:
        return """
Usage: @namecheck /<username> <optional limit>
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        print(message)
        # if zuliprc() and message['stream_id'] != username_stream():
        #     bot_handler.send_reply(message, "This bot only works in the username stream.")
        #     return

        args: list[str] = message['content'].split(" ")

        if not args or not args[0].startswith("/"):
            bot_handler.send_reply(message, self.usage())
            return

        results = find_most_similar_already_discussed(args[0], int(args[1]) if len(args) > 1 else 10)
        bot_handler.send_reply(
            message,
            f"{len(results)} most similar:\n" + ", ".join(results)
        )

handler_class = NameCheckHandler
