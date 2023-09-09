# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

###    inputs
#url = input('Enter URL: ')
#count = input('Enter count:')
#position = input('Enter position:')



###    testing variables
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = 4
url2 = None
#Beautiful soup
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    position = 3
    for tag in tags:
        tag = tag.get('href', None)
        position = position - 1
        if position == 0:
            url = tag
            break
            #print(url)
    print(url)
    count = count -1
    print('count:',count)
            