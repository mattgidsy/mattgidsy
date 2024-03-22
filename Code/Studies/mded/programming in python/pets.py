# import random

# #f_name = input('Type the file name:')
# f_name = 'petnames.txt'
# with open(f'programming in python/{f_name}','r') as file:
#     data = file.read()
#     data_lst = data.split()
    
# print(random.choice(data_lst))    

new_list = [1,2,3,4]

# new_list[4] = 10
new_list.extend(new_list)
print(new_list)
new_list.insert(0, 0)
print(new_list)
new_list.append(5)
print(new_list)