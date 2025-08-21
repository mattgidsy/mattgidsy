import requests
from bs4 import BeautifulSoup

def decode_google_doc_table(doc_url):
    # Convert published Google Doc URL to HTML export
    if "/pub" in doc_url:
        doc_url = doc_url.replace("/pub", "/pub?embedded=true")

    response = requests.get(doc_url)
    if response.status_code != 200:
        print("Failed to fetch the document.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if not table:
        print("No table found in the document.")
        return

    points = []
    # Parse rows (skip header)
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) == 3:
            try:
                x = int(cols[0].text.strip())
                char = cols[1].text.strip()
                y = int(cols[2].text.strip())
                points.append((x, y, char))
            except ValueError:
                continue

    if not points:
        print("No valid character data found.")
        return

    # Figure out grid size
    max_x = max(x for x, y, c in points)
    max_y = max(y for x, y, c in points)

    # Build empty grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Populate grid with y-flip
    for x, y, char in points:
        flipped_y = max_y - y
        grid[flipped_y][x] = char

    # Print top-to-bottom as-is
    for row in grid:
        print("".join(row))
        
# Example usage:
decode_google_doc_table(
    "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
)
