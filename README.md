# Username similarity

A repo to check if a given username if similar to a username already discussed on zulip.
This uses word llama embeddings.

## Local Development

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Test messages + responses using the bot emulator

```bash
zulip-bot-shell namecheck.py

# > Enter your message:
# try "/jones" or "/smith 3"
```

## Docker

Test docker build locally:

```bash
docker build -t zulipbot .
```

```bash
docker run -it --rm \
    -v ~/Downloads/zuliprc:/zuliprc \
    -e ZULIPRC=/zuliprc \
    zulipbot

## to test on a local zulip server, you can set a custom stream ID
docker run -it --rm \
    -v ~/Downloads/zuliprc:/zuliprc \
    -e ZULIPRC=/zuliprc \
    -e USERNAME_STREAM=4 \
    zulipbot
```
