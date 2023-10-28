s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
s_lst = s.split()

num_vowels = 0

for word in s_lst:
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                num_vowels += 1

print(num_vowels)    

#chat's way:
# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a', 'e', 'i', 'o', 'u']

# num_vowels = 0

# for letter in s:
#     if letter in vowels:
#         num_vowels += 1

# print(num_vowels)