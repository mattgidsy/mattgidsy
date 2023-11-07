ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def lst_search(lst):
    for word in lst:
        return word[1]
    
lambda_sort = sorted(ex_lst, key= lambda x: lst_search(x))
print(lambda_sort)