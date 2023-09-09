# Use words.txt as the file name
#prompt for file name
# print the contents in uppercase
#make sure to rstrip
fname = input("Enter file name: ")
fhandle = open(fname)
for line in fhandle :
    line = line.rstrip()
    print(line.upper()) 