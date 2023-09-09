# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
total = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        count = count + 1
        stnumber = line.find(' ')
        confnumber = line[stnumber:]
        fconfnumber = float(confnumber)
        total = total+fconfnumber
        #print(total)
        continue
print("Average spam confidence:", total/count)

