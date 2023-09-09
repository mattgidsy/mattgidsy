import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

###    inputs
url = input('Enter URL: ')
icount = input('Enter count:')
iposition = input('Enter position:')
count = int(icount)


print('Retrieving:',url)
while count > 0:
    ###    Beautiful soup ju ju
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    position = int(iposition)
    for tag in tags:
        tag = tag.get('href', None)
        position = position - 1
        if position == 0:
            url = tag
            break
    print('Retrieving:',url)
    count = count -1
            