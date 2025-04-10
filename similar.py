from faker import Faker
import re
from wordllama import WordLlama
import zulip

from config import username_stream, zuliprc


topic_prefix = r"^/|^✔ /"

def get_usernames() -> list[str]:
    if zuliprc():
        client = zulip.Client(config_file=zuliprc())
        stream_id = client.get_stream_id(username_stream())["stream_id"]
        result = client.get_stream_topics(stream_id)
        username_topics = [uname["name"] for uname in result["topics"] if re.match(topic_prefix, uname["name"])]
    else:
        fake = Faker()
        username_topics = [f"/{fake.name()}" for _ in range(1000)]
    return username_topics


def find_most_similar_already_discussed(name_in_question: str, limit: int) -> list[str]:
    usernames = get_usernames()
    wl = WordLlama.load()
    return wl.topk(name_in_question, usernames, k=limit)
