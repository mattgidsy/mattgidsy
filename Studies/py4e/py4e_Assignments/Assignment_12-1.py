from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_1876859.html" 
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count=0
comments = list()

for tag in tags:
    comment = int(tag.contents[0])
    comments.append(comment)
    count = count+1
    
print("Count",count)
print("Sum",sum(comments))