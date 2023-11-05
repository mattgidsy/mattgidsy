def test(i, b = True, dict1 = {2:3, 4:5, 6:8}):
    if b == True:
        if i in dict1.keys():
            return dict1[:i]
    else:
        return b == False