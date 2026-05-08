import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_notion_price():
    url = "https://www.notion.com/pricing"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch Notion. Status: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    plans = soup.find_all("article")

    for plan in plans:
        name = plan.find("h3")
        price = plan.find("span")

        if name and "Plus" in name.text:
            return {
                "platform": "Notion",
                "plan": "Plus",
                "price": price.text.strip(),
                "date": str(date.today())
            }

    return None

print(fetch_notion_price())