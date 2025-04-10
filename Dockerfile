FROM python:3.13.2-bookworm

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /python-zulip-api/zulip_bots/zulip_bots/bots/namecheck/

WORKDIR /python-zulip-api/zulip_bots/zulip_bots/bots/namecheck

ENV ZULIPRC=/zuliprc

ENTRYPOINT \
    COMMIT_HASH=$(git rev-parse --short HEAD) \
    LAST_COMMIT=$(git log -1 --pretty="%ad %s") \
    zulip-run-bot namecheck.py --config-file $ZULIPRC
