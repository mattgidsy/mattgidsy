Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for course in Junior:
    credits = credits + Junior[course]
##   
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1
##
s1 = "hello"
counts = {}

for char in s1:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1
    
##
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
str1_words = str1.split()

for word in str1_words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
##
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
sent_words = sent.split()

for word in sent_words:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
    
##
sally = "sally sells sea shells by the sea shore"
characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1

char_lst = list(characters.keys())
char_var = char_lst[0]

for best_char in char_lst:
    if best_char < char_var:
        best_char = char_var
print(best_char)
##
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1

char_lst = list(characters.keys())
worst_char = char_lst[0]

for key in char_lst:
    if characters[key] < characters[worst_char]:
        worst_char = key
##
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1_low = string1.lower()
letter_counts = {}

for char in string1_low:
    if char not in letter_counts:
        letter_counts[char] = 0
    letter_counts[char] += 1
print(letter_counts)

##
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for char in p.lower():
    if char not in low_d:
        low_d[char] = 0
    low_d[char] += 1
print(low_d)