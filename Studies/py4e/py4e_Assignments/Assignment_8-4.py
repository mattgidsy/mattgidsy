fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    list = line.split()
    for word in list:
        if word[0] != word[1]:
            lst.append(word[0])
        
    #print(line)
print(lst)
    
