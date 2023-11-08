with open("Code\Studies\p3p\scarlet.txt") as scarlet:
    cont = scarlet.read()
count_dict = {}

for char in cont:
    
    if char not in count_dict:
        count_dict[char] = 0
    
    count_dict[char] += 1


for letter_count in sorted(count_dict.items()):
    print(f"letter {letter_count[0]} found {letter_count[1]} times")