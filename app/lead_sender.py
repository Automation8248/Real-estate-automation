import csv, json
from app.history import is_sent, mark_sent
from app.gmail_smtp import send_email

POOL="data/lead_pool_master.csv"
CLIENTS="state/clients.json"

def pick_unsent(n):
    out=[]
    with open(POOL,"r",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not is_sent(r["lead_id"]):
                out.append(r)
                if len(out)>=n: break
    return out

def send_demo(email):
    leads=pick_unsent(5)
    body="\n".join([l["name"]+" "+l["city"] for l in leads])
    send_email(email,"Your Demo Leads",body)
    for l in leads:
        mark_sent(l["lead_id"],email)

def run_weekly():
    clients=json.load(open(CLIENTS))["clients"]
    for c in clients:
        if c["status"]!="ACTIVE": continue
        leads=pick_unsent(50)
        body="\n".join([l["name"]+" "+l["city"] for l in leads])
        send_email(c["email"],"Weekly Leads",body)
        for l in leads:
            mark_sent(l["lead_id"],c["email"])
          
