#find top 10 common words the long way
file_name = input('Enter a file:')
file_handle = open(file_name)
#make a counter dicitonary
counts = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        #make each item of count dictionary hold the pair of items [word,0] (word being the word) 0 being the counter
        counts[word] = counts.get(word, 0) +1
        
lst = list()
for key, val in counts.items():
#This flips the key and value of the dictionary and saves it to a new list
    newtup = (val, key)
    lst.append(newtup)
    
#use the sort function on the new list you made
lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
    print(key,val)