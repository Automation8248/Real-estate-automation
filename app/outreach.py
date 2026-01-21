import csv, datetime
from app.ai_qwen import outreach_msg
from app.gmail_smtp import send_email

FILE="state/prospects.csv"

def follow_up_needed(last):
    if not last: return False
    return (datetime.date.today()-datetime.date.fromisoformat(last)).days>=5

def run():
    rows=[]
    with open(FILE,"r",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    for r in rows:
        if r["status"]=="NEW":
            send_email(r["email"],"Free Demo Leads",outreach_msg(r["business_name"],r["city"],r["country"]))
            r["status"]="CONTACTED"
            r["last_contacted"]=str(datetime.date.today())
        elif r["status"]=="CONTACTED" and follow_up_needed(r["last_contacted"]):
            send_email(r["email"],"Follow up – Free Leads",outreach_msg(r["business_name"],r["city"],r["country"]))
            r["last_contacted"]=str(datetime.date.today())
    with open(FILE,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
                                                                        
