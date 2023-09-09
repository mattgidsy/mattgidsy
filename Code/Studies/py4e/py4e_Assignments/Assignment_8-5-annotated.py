
fname = input("Enter file name: ")
#open the file mbox-short.txt
#if len(fname) < 1:
    #fname = "mbox-short.txt"
fh = open(fname)
#start a count
count = 0
# read the document line by line (for ____ in *handle*)
for line in fh:
    #add the condition to only parse "From " lines
    if line.startswith("From "):
        #count that mf
        count = count +1
        #strip the lines to split correctly
        line.rstrip()
        #split for indices
        words = line.split()
        #identify the email by index number
        email = words[1]
        print(email)


print("There were", count, "lines in the file with From as the first word")
