import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

# Base URL
BASE_URL = "https://books.toscrape.com/"

# CSV file name
CSV_FILE = "books_data.csv"

# Store all books
books_data = []

# Current page URL
current_page = BASE_URL

while current_page:

    try:
        print(f"Scraping: {current_page}")

        response = requests.get(current_page, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            # Title
            title_tag = book.find("h3").find("a")
            title = title_tag.get("title", "N/A")

            # Product URL
            product_url = urljoin(current_page, title_tag.get("href", ""))

            # Price
            price_tag = book.find("p", class_="price_color")
            price = price_tag.text.strip() if price_tag else "N/A"

            # Rating
            rating_tag = book.find("p", class_="star-rating")

            if rating_tag:
                classes = rating_tag.get("class", [])
                rating = classes[1] if len(classes) > 1 else "N/A"
            else:
                rating = "N/A"

            # Availability
            availability_tag = book.find(
                "p",
                class_="instock availability"
            )

            availability = (
                availability_tag.text.strip()
                if availability_tag else "N/A"
            )

            books_data.append([
                title,
                price,
                rating,
                availability,
                product_url
            ])

        # Find next page
        next_button = soup.find("li", class_="next")

        if next_button:
            next_page = next_button.find("a")["href"]
            current_page = urljoin(current_page, next_page)
        else:
            current_page = None

        # Delay between requests
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print("HTTP Error:", e)
        break

# Save data to CSV
with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Price",
        "Rating",
        "Availability",
        "URL"
    ])

    writer.writerows(books_data)

print(f"\nData saved successfully in {CSV_FILE}")
print(f"Total books scraped: {len(books_data)}")