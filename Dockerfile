FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV BOT_TOKEN my-bot-token
ENV CHAT_ID my-chat-id

CMD ["python", "main.py"]