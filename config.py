import os


def username_stream() -> int:
    return int(os.getenv("USERNAME_STREAM", 91))


def zuliprc():
    return os.getenv("ZULIPRC")
