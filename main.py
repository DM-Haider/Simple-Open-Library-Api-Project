import csv
import requests

API_URL = "https://openlibrary.org/search.json"
MAX_BOOKS = 50
MIN_PUBLICATION_YEAR = 2000
OUTPUT_FILE = "books_after_2000.csv"


def fetch_books(limit):
    """
    Fetch books data from OpenLibrary API.
    """
    try:
        response = requests.get(
            API_URL, params={"q": "python", "limit": limit}, timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("docs", [])
    except requests.RequestException as error:
        print(f"Error fetching data from API: {error}")
        return []


def filter_books_by_year(books, min_year):
    """
    Filter books published after a specific year.
    """
    filtered_books = []

    for book in books:
        publish_years = book.get("first_publish_year")
        if not publish_years:
            continue

        if publish_years > min_year:
            filtered_books.append(
                {
                    "title": book.get("title", "N/A"),
                    "author": ", ".join(book.get("author_name", ["Unknown"])),
                    "publish_year": publish_years,
                    "edition_count": book.get("edition_count", 0),
                }
            )

    return filtered_books


def export_to_csv(books, file_path):
    """
    Export filtered books to CSV file.
    """
    if not books:
        print("No books to export.")
        return

    fieldnames = ["title", "author", "publish_year", "edition_count"]

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)

        print(f"Data successfully saved to {file_path}")

    except IOError as error:
        print(f"Error writing to CSV file: {error}")


def main():
    """
    Main execution flow.
    """
    print("Fetching books from OpenLibrary API...")

    books = fetch_books(MAX_BOOKS)
    filtered_books = filter_books_by_year(books, MIN_PUBLICATION_YEAR)

    print(f"Total books fetched: {len(books)}")
    print(f"Books published after {MIN_PUBLICATION_YEAR}: {len(filtered_books)}")

    export_to_csv(filtered_books, OUTPUT_FILE)


if __name__ == "__main__":
    main()
