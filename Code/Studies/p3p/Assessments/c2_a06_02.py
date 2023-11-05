def check_nums(lst):
    no7 = True
    sub = []
    while no7 == True:
        for var in lst:
            if var != 7:
                sub.append(var)
            else:
                no7 = False
                break
    return sub
        

lst1 = [1,2,3,4,5,6,7,8,9]

output = check_nums(lst1)
print(output)