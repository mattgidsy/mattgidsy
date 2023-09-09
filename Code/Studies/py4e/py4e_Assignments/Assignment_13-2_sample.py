import urllib.request, urllib.parse, urllib.error
import json
import ssl

#def fetch_and_parse_json(url)
    #try:

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1876862.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
        
handle = urllib.request.urlopen(url, context=ctx)
info = handle.read().decode()
data = json.loads(info)
scount = 0
print('Retrieving:', url)
print('Retrieved:', len(info),'characters')
print('Count:', len(data['comments']))
#print(data)
#print(json.dumps(data, indent=4))
for comment in data['comments']:
    icount = int(comment['count'])  
    scount += icount
    #print('Comment',comment['count'])
print('Sum:', scount)

        
        










#if __name__ == "__main__":
    #url = input('Enter location:')
   #fetch_and_parse_json(url)