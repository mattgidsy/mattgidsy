import urllib.request, urllib.parse, urllib.error
import json
import ssl

#url = 'http://py4e-data.dr-chuck.net/comments_1876862.json'
# Chat said to only add a way to validate the URL. Great Job!! They gave me compliments!

def fetch_and_parse_json(url):
    try:
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL. Please enter a URL starting with 'http://' or 'https://'.")

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        # Fetch and parse the json
        handle = urllib.request.urlopen(url, context=ctx)
        info = handle.read().decode()
        data = json.loads(info)
        scount = 0
        print('Retrieving:', url)
        print('Retrieved:', len(info),'characters')
        print('Count:', len(data['comments']))
        
        # Find sum of comment count
        for comment in data['comments']:
            icount = int(comment['count'])  
            scount += icount
        print('Sum:', scount)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input('Enter location:')
    fetch_and_parse_json(url)