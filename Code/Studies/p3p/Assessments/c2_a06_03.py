def sublist(str_lst):
    sub = []
    stop = True
    while stop == True:
        for val in str_lst:
            if val == "STOP":
                stop = False
                break
            else:
                sub.append(val)
    return sub
                
                
    