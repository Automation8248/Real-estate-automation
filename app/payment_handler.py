import json, datetime
from app.gmail_imap import fetch_paypal

FILE="state/clients.json"

def run():
    data=json.load(open(FILE))
    for p in fetch_paypal():
        email=p["payer"]
        data["clients"].append({
            "email":email,
            "plan":"PRO",
            "status":"ACTIVE",
            "start":str(datetime.date.today()),
            "end":str(datetime.date.today()+datetime.timedelta(days=30)),
            "sent":0
        })
    json.dump(data,open(FILE,"w"),indent=2)
  
