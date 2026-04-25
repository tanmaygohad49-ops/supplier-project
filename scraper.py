import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 4):
    url = BASE_URL.format(page)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    books = soup.select(".product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()

        data.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    time.sleep(1)

with open("../data_raw.json", "w") as f:
    json.dump(data, f, indent=4)

print("Done. Total:", len(data))