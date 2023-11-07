def mult(i,i_str =6):
    return i*i_str

#2
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
#3
def sum(intx,intz=5):
    return intz + intx
#4
def test(i,b = True, dict1 = {2:3,4:5,6:8}):
    if b == True:
        for k in dict1:
            if k == i:
                return dict1[k]
    else:
        return False
#5
def checkingIfIn(key, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:  # Check if key is a key in d
        return key in d
    else:  # Check if key is not a key in d
        return key not in d
    
