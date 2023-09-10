# This is a big fat party tester
# Ask if a they are a party animal
# Scrape data from a lyrics site that will print party for every instance of party in "Party Hard"
# Rick roll the non-party animals
import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#parse the website for lyrics
def soup_to_text():
    url = "https://www.azlyrics.com/lyrics/andrewwk/partyhard.html"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    words = text.split()
    song_a = words.index("When")
    song_z = words.index("Submit")
    song = words[song_a:song_z]
    return (song)
    
    #song = words[44:319]

### write loop for the party in song
soup_to_text()
song = soup_to_text()

def party_harty():
    for party in song:
        if party == "party":
            print("party")

        
        
its_time_to_party = input("Are you a party animal? 'Y' or 'N'")
we_will_party_hard = None

class PartyAnimal():
    def party(self):
        print("When it's time to party we will party hard.")
        party_harty()
        
    def noparty(self):
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
              
andrew = PartyAnimal()
    
if its_time_to_party == "Y":
    andrew.party()

else:
    andrew.noparty()
