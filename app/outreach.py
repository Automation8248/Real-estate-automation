import csv, datetime, os
from app.ai_qwen import outreach_msg
from app.gmail_smtp import send_email

FILE="state/prospects.csv"
FIELDS=["business_name","email","city","country","topic","status","last_contacted"]

def ensure_file():
    os.makedirs("state", exist_ok=True)
    if not os.path.exists(FILE):
        with open(FILE,"w",encoding="utf-8",newline="") as f:
            w=csv.writer(f)
            w.writerow(FIELDS)

def follow_up_needed(last):
    if not last:
        return False
    try:
        return (datetime.date.today()-datetime.date.fromisoformat(last)).days >= 5
    except:
        return False

def run():
    ensure_file()

    # load rows
    with open(FILE,"r",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))

    # ✅ If file empty, just return (no crash)
    if not rows:
        return

    for r in rows:
        status = (r.get("status") or "NEW").strip()

        if status == "NEW":
            send_email(
                r["email"],
                "Free Demo Leads",
                outreach_msg(r["business_name"], r["city"], r["country"])
            )
            r["status"]="CONTACTED"
            r["last_contacted"]=str(datetime.date.today())

        elif status == "CONTACTED" and follow_up_needed(r.get("last_contacted","")):
            send_email(
                r["email"],
                "Follow up – Free Leads",
                outreach_msg(r["business_name"], r["city"], r["country"])
            )
            r["last_contacted"]=str(datetime.date.today())

    # save back safely
    with open(FILE,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
