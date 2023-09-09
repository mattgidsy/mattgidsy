import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/comments_1876861.xml"
url = input('Enter location:')
xml = urllib.request.urlopen(url)
data = xml.read()
root = ET.fromstring(data)
counts = root.findall('.//count')
scount = 0
print('Retrieved', len(data), 'characters')
print('Count',len(counts))

for comment in root.findall('.//comment'):
    count = comment.find('count').text
    icount = int(count)
    scount = scount + icount
    
print('Sum:',scount)