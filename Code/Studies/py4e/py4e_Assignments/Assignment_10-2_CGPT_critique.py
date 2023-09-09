from collections import defaultdict

e_counter = defaultdict(int)

with open('mbox-short.txt') as handle:
    for line in handle:
        if line.startswith("From "):
            line = line.rstrip()
            _, _, _, _, _, time, _ = line.split()  # Unpack directly
            hour, _, _ = time.split(":")  # Unpack directly
            e_counter[hour] += 1

for key, val in sorted(e_counter.items()):
    print(key, val)