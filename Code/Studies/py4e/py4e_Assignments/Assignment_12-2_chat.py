import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_url_from_user():
    while True:
        url = input('Enter URL: ')
        if url.startswith('http://') or url.startswith('https://'):
            return url
        else:
            print('Invalid URL. Please include "http://" or "https://".')
            
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Invalid input. Please enter an integer.')

def retrieve_and_follow_links(url, count, position):
    while count > 0:
        try:
            print('Retrieving:', url)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            
            if position <= len(tags):
                url = tags[position - 1].get('href', None)
                count -= 1
            else:
                print('Position exceeds the number of links on the page.')
                break
        except Exception as e:
            print('Error:', e)
            break

if __name__ == '__main__':
    url = get_url_from_user()
    count = get_integer_input('Enter count: ')
    position = get_integer_input('Enter initial position: ')

    retrieve_and_follow_links(url, count, position)