import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')

print('Retrieving:', url)

for i in range(0,int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve tags
    tags = soup('a',limit=int(position))
    for tag in tags:
        url = tag.get('href',None)
    print('Retrieving:', tag.get('href',None))