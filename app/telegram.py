import os, requests

def send(token, chat_id, msg):
    if not token: return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": msg})

def bot1(msg):
    send(os.getenv("TELEGRAM_BOT1_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"), msg)

def bot2(msg):
    send(os.getenv("TELEGRAM_BOT2_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"), msg)
  
