sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0
num_ae_lst = []
sentence_lst = sentence.split()
for word in sentence_lst:
    for letter in word:
        if letter[:] == "a":
            num_ae_lst.append(word)
            num_a_or_e += 1
            break
        elif letter[:] == "e":
            num_ae_lst.append(word)
            num_a_or_e += 1
            break

print(num_a_or_e)
        