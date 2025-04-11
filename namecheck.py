from typing import Any, Dict
from zulip_bots.lib import BotHandler

from config import last_commit, username_stream, version, zuliprc
from similar import find_most_similar_already_discussed


def format_results(results: list[str]) -> str:
    channel = username_stream()
    return ", ".join(f"#**{channel}>{result}**" for result in results)


class NameCheckHandler:
    def usage(self) -> str:
        commit_url = f"https://github.com/lichess-org/namecheck/commit/{version()}"
        return f"""
Usage: `@NameCheck <search> <optional limit>`

Version: [{version()}]({commit_url}) {last_commit()}
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        print(message)
        # if zuliprc() and message['stream_id'] != username_stream():
        #     bot_handler.send_reply(message, "This bot only works in the username stream.")
        #     return

        args: list[str] = message["content"].split(" ")

        if not args or args[0] == "help":
            bot_handler.send_reply(message, self.usage())
            return

        results = find_most_similar_already_discussed(
            args[0], int(args[1]) if len(args) > 1 else 10
        )
        bot_handler.send_reply(
            message, f"{len(results)} most similar:\n" + format_results(results)
        )


handler_class = NameCheckHandler
