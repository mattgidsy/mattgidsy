handle = open('mbox-short.txt')
e_counter = dict()

for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        e_line = line.split()
        time = e_line[5]
        intv = time.split(":")
        hour = intv[0]
        e_counter[hour] = e_counter.get(hour,0)+1


for key,val in sorted(e_counter.items()):
    print(key,val)