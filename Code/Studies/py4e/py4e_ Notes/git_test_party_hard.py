# This is a big fat party tester
# Ask if a they are a party animal
# Scrape data from a lyrics site that will print party for every instance of party in "Party Hard"
# Rick roll the non-party animals
import bs4
import ssl
import urllib


its_time_to_party = input("Are you a party animal? 'Y' or 'N'")
we_will_party_hard = None

class PartyAnimal():
    def party(self):
        print("When it's time to party we will party hard.")
        
    def noparty(self):
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
              
andrew = PartyAnimal()
    
if its_time_to_party == "Y":
    andrew.party()

else:
    andrew.noparty()
