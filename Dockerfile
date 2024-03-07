FROM python:3.11-alpine
RUN mkdir /botyushka_bot
WORKDIR /botyushka_bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
