import os
import requests
from bs4 import BeautifulSoup

# Read env vars with defaults
SEARCH_TERM = os.getenv("SEARCH_TERM", "DevOps")
FILTER_COUNTRIES = [c.strip() for c in os.getenv("FILTER_COUNTRIES", "India").split(",")]

URL = f"https://jobs.aligntech.com/search-job?search={SEARCH_TERM}"

def fetch_jobs():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for row in soup.select(".rt-tr-group"):
        title_tag = row.select_one("a.text-bold")
        location = row.get("data-location") or row.find("div", {"title": True})

        if not title_tag or not location:
            continue

        title = title_tag.get_text(strip=True)
        location = row.get("data-location") or location.get_text(strip=True)
        link = "https://jobs.aligntech.com" + title_tag.get("href")

        # Exclude jobs in certain countries
        if any(country in location for country in FILTER_COUNTRIES):
            continue

        jobs.append({
            "title": title,
            "location": location,
            "url": link
        })

    return jobs

if __name__ == "__main__":
    print(f"Searching for: {SEARCH_TERM}")
    print(f"Excluding countries: {', '.join(FILTER_COUNTRIES)}\n")

    jobs = fetch_jobs()
    if jobs:
        print("New vacancies found:")
        for job in jobs:
            print(f"- {job['title']} ({job['location']}) → {job['url']}")
    else:
        print("No suitable vacancies found outside excluded countries.")