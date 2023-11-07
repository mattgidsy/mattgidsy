#1
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse =True)

#2
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
#3
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals.keys())
# #4
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
sorted_medals = sorted(medals, reverse =True, key=lambda x: medals[x])
i = 0
top_three = []
for country in sorted_medals:
    if i < 3:
        i +=1
        top_three.append(country)
#5
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, key =lambda v: groceries[v],reverse =True)
#6
def last_four(x):
    xstr = str(x)
    return xstr[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
idict = {}

for i in ids:
    four_id = last_four(i)
    idict[i] = four_id
    
sorted_ids = sorted(idict)   
print(sorted_ids)
#7
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key =lambda x: x) 
#8
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda x: x[1])