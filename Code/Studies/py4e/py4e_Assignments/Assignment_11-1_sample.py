import re
handle = open("regex_sum_42.txt")
nums = re.findall('[0-9]+', handle.read())
inums=list()
for num in nums:
    num = int(num)
    inums.append(num)

print(sum(inums))

