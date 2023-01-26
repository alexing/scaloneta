FROM python:3.9-slim

COPY bot/football_api.py /bot/
COPY bot/main.py /bot/
COPY bot/twitter.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "main.py"]
