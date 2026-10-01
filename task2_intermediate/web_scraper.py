"""ShadowFox Python Internship - Task 2: Web Scraper

Default target: https://quotes.toscrape.com/
The task brief suggests using Beautiful Soup or Scrapy and saving
scraped data. The URL is configurable so the scraper can also be
used with another permitted practice website.
"""

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
OUTPUT = Path("scraped_quotes.csv")

def scrape_quotes(url: str):
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ShadowFoxInternshipBot/1.0)"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = []

    for quote in soup.select("div.quote"):
        text = quote.select_one("span.text")
        author = quote.select_one("small.author")
        tags = [tag.get_text(strip=True) for tag in quote.select("a.tag")]

        if text and author:
            rows.append({
                "quote": text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": ", ".join(tags),
            })

    return rows

def save_csv(rows, output_path: Path):
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    try:
        data = scrape_quotes(URL)
        save_csv(data, OUTPUT)
        print(f"Scraped {len(data)} quotes.")
        print(f"Saved to: {OUTPUT.resolve()}")
    except requests.RequestException as exc:
        print("Could not access the website:", exc)
    except Exception as exc:
        print("Unexpected scraping error:", exc)
