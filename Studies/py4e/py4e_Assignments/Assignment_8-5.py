
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        count = count +1
        line.rstrip()
        words = line.split()
        email = words[1]
        print(email)


print("There were", count, "lines in the file with From as the first word")
