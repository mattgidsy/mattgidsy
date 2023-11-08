
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_lst = sent.split()
acro = ""
for word in sent_lst:
    if word in stopwords:
        sent_lst.remove(word)
for word in sent_lst:
     acro = acro + word[:2].upper() + ". "
if acro[-2:] == ". ":
    acro = acro[:-2]


print(acro)