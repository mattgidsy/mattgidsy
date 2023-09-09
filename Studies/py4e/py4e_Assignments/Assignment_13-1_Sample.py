import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = input('Enter location:')

xml = urllib.request.urlopen(url)
data = xml.read()
root = ET.fromstring(data)
print('Retrieved', len(data), 'characters')
#print(data.decode())
counts = root.findall('.//count')
print('Count',len(counts))
scount = 0
for comment in root.findall('.//comment'):
    count = comment.find('count').text
    icount = int(count)
    scount = scount + icount
    #print(icount)
print('Sum:',scount)