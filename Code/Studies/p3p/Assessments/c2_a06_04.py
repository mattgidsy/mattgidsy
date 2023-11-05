def stop_at_z(str_lst):
    noz = True
    sub = []
    while noz == True:
        for val in str_lst:
            if val == "z":
                noz = False
                break
            else:
                sub.append(val)
    return sub