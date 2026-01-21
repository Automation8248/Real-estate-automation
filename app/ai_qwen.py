import os, requests

def qwen(prompt):
    key = os.getenv("HF_API_KEY")
    model = os.getenv("HF_MODEL","Qwen/Qwen2.5-7B-Instruct")
    if not key: return ""
    r = requests.post(
        f"https://api-inference.huggingface.co/models/{model}",
        headers={"Authorization": f"Bearer {key}"},
        json={"inputs": prompt},
        timeout=60
    )
    data = r.json()
    if isinstance(data,list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    return ""

def outreach_msg(business, city, country):
    prompt = f"Write short email offering 5 free real estate leads to {business} in {city}, {country}"
    return qwen(prompt) or f"Hi {business}, I can share 5 free real estate leads for your area. Reply YES for demo."

def auto_reply(user_msg):
    prompt = f"Reply politely to client message:\n{user_msg}"
    return qwen(prompt) or "Thanks! I will send demo leads shortly."
  
