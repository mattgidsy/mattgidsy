scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_lst = scores.split()
a_scores_lst = []

for score in scores_lst:
    int_score = int(score)
    if int_score >= 90:
        a_scores_lst.append(int_score)

a_scores = len(a_scores_lst)
       
print(a_scores)