def beginning(str_lst):
    nobye = True
    sub = []
    while nobye == True:
        for val in str_lst:
            if val == "bye":
                nobye = False
                break
            else:
                sub.append(val)
    return sub[:10]