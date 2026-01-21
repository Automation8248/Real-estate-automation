import csv
from datetime import datetime

HISTORY="data/sent_leads_history.csv"

def is_sent(lead_id):
    with open(HISTORY,"r",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["lead_id"]==lead_id:
                return True
    return False

def mark_sent(lead_id, email):
    with open(HISTORY,"a",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow([lead_id,email,datetime.utcnow().isoformat()])
      
