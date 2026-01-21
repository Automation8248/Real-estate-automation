import csv, uuid, random, datetime, os

MASTER="data/lead_pool_master.csv"
OUTDIR="data/generated_leads"

def generate_leads(count=500):
    os.makedirs(OUTDIR, exist_ok=True)  # ✅ ADD THIS LINE

    today=str(datetime.date.today())
    fname=f"{OUTDIR}/{today}.csv"

    leads=[]
    for _ in range(count):
        lead_id=str(uuid.uuid4())
        city=random.choice(["Delhi","Mumbai","New York","London"])
        leads.append([lead_id,f"Owner {random.randint(1,9999)}","+91XXXXXXXXXX","",city,"IN","Seller","Generated"])

    with open(fname,"w",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow(["lead_id","name","phone","email","city","country","type","notes"])
        w.writerows(leads)

    with open(MASTER,"a",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerows(leads)

    return fname
