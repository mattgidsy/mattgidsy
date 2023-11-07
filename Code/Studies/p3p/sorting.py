#########
# #sort by second letter function 
# def second_let(word):
#     return word[1]
    
# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
# sorted_by_second_let = sorted(ex_lst, key =second_let)

#########
# #sort by lst letter function
# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

# def last_char(word):
#     return word[-1]
    

# nums_sorted = sorted(nums, reverse =True, key =last_char)

#########
# #as a lambda function
# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

# nums_sorted_lambda = sorted(nums, reverse =True, key=(lambda nums: nums[-1]))

# Sorting dictionary by keys
# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# sorted_medals = sorted(medals, reverse =True, key=lambda x: medals[x])
# i = 0
# for country in sorted_medals:
#     if i < 3:
#         i +=1
#         print(country)