import urllib.request
from bs4 import BeautifulSoup
import ssl
import csv

# The URL of the website containing the HTML table
url = 'https://www.utep.edu/herbal-safety/populations/herbs-to-avoid-during-pregnancy.html'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Send an HTTP GET request to the website
try:
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print(f'Failed to retrieve the web page: {url}')
    exit()

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the HTML table you want to extract, assuming it has a 'table' tag
table = soup.find('table')

if table:
    # Create a CSV file to write the table data
    with open('herb_preg_data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Find all the rows in the table
        rows = table.find_all('tr')

        for row in rows:
            # Extract the data from each cell in the row
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(strip=True) for cell in cells]
            csv_writer.writerow(row_data)

    print('Table data has been successfully exported to "table_data.csv"')
    
else:
    print('No table found on the web page.')
print(table)