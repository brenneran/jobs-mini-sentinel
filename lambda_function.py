from align_devops import fetch_jobs
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(message: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ BOT_TOKEN or CHAT_ID not set")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def lambda_handler(event, context):
    jobs = fetch_jobs()
    if jobs:
        msg = "\n".join([f"- {job['title']} ({job['location']}) → {job['url']}" for job in jobs])
        send_to_telegram(f"✅ New vacancies found:\n{msg}")
        return {"jobs": jobs}
    else:
        send_to_telegram("❌ No suitable vacancies found outside excluded countries.")
        return {"message": "No suitable vacancies found."}