def sublist(lst):
    sub = []
    for val in lst:
        if val == 5:
            break
        else:
            sub.append(val)    
    return sub
lst1 = [1,2,3,4,5,6,7]

output = sublist(lst1)
print(output)