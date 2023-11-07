def check_nums(numbers_list,stop_num):
    result = []
    i = 0
    

    while i < len(numbers_list) and numbers_list[i] != stop_num:
        result.append(numbers_list[i])
        i += 1

    return result

# Example usage:

numbers = [1, 2, 4, 6, 7, 9, 3, 5]
result_list = check_nums(numbers,7)
print(result_list)