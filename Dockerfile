FROM python:3.13.2-slim-bookworm

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /python-zulip-api/zulip_bots/zulip_bots/bots/namecheck/

WORKDIR /python-zulip-api/zulip_bots/zulip_bots/bots/namecheck

ENTRYPOINT zulip-run-bot namecheck.py --config-file /zuliprc
