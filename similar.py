from faker import Faker
import re
import wordninja
from wordllama import WordLlama
import zulip

from config import username_stream, zuliprc


topic_prefix = r"^/|^✔ /"


def get_usernames() -> list[str]:
    if zuliprc():
        client = zulip.Client(config_file=zuliprc())
        stream_id = client.get_stream_id(username_stream())["stream_id"]
        result = client.get_stream_topics(stream_id)
        username_topics = [
            uname["name"]
            for uname in result["topics"]
            if re.match(topic_prefix, uname["name"])
        ]
    else:
        fake = Faker()
        username_topics = [f"/{fake.user_name()}" for _ in range(1000)]
        username_topics += [f"✔ /{fake.user_name()}" for _ in range(1000)]
    return username_topics


def segment(name: str) -> str:
    return " ".join(wordninja.split(name))


def find_most_similar_already_discussed(name_in_question: str, limit: int, exact=False) -> list[str]:
    usernames = [name for name in get_usernames() if name != name_in_question]
    if exact:
        usernames = [name for name in usernames if name_in_question.lower() in name.lower()]
    if len(usernames) <= limit:
        # might happen if looking for exact matches.
        return usernames

    wl = WordLlama.load()
    query_embedding = wl.embed(segment(name_in_question))
    doc_embeddings = wl.embed([segment(name) for name in usernames])
    scores = wl.vector_similarity(query_embedding[0], doc_embeddings).squeeze()
    ranked = sorted(zip(usernames, scores.tolist()), key=lambda pair: pair[1], reverse=True)
    return [name for name, _score in ranked[:limit]]
