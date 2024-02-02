import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} #set up empty dictionary for query params
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3"
    resp = requests.get(baseurl, params=params_diction)
    words_ds = resp.json()
    return [d['word'] for d in words_ds]
    return resp.json() #return python object( list of dicts)

print(get_rhymes("funny"))
print(get_rhymes("dash"))