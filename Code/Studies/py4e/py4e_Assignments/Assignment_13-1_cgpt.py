import urllib.request
import xml.etree.ElementTree as ET
import ssl

def fetch_and_parse_xml(url):
    try:
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        xml = urllib.request.urlopen(url, context=ctx)
        data = xml.read()
        root = ET.fromstring(data)
        counts = root.findall('.//count')
        scount = 0

        print('Retrieved', len(data), 'characters')
        print('Count', len(counts))

        for comment in root.findall('.//comment'):
            count = comment.find('count').text
            icount = int(count)
            scount += icount

        print('Sum:', scount)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input('Enter location:')
    fetch_and_parse_xml(url)
