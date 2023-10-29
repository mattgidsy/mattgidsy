
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

org_lst = org.split()
acro = ""
for word in org_lst:
    if word in stopwords:
        org_lst.remove(word)
for word in org_lst:
    acro = acro + word[0].upper()

print(org_lst)
print(acro)
        