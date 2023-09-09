from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_42.html" 
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count=0
comments = list()
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get(tag, None))
    #print('comments:', tag.contents[0])
    comment = int(tag.contents[0])
    comments.append(comment)
    count = count+1
    
    #print('Attrs:', tag.attrs)
    #print(" ")
print(count)
print(sum(comments))