sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

sentence_lst = sentence.split()
same_letter_lst = []

for word in sentence_lst:
    word_a = word[0]
    word_z = word[-1]
    if word_a == word_z:
        same_letter_lst.append(word)
        
same_letter_count = len(same_letter_lst)
print(same_letter_count)