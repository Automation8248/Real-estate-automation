from app.gmail_imap import fetch_unseen
from app.gmail_smtp import send_email
from app.ai_qwen import auto_reply
from app.lead_sender import send_demo

def run():
    for r in fetch_unseen():
        send_email(r["from"],"Re: Demo Leads",auto_reply(r["body"]))
        if "yes" in r["body"].lower():
            send_demo(r["from"])
          
