
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1= ""
        n2 = ""
        l1.reverse()
        l2.reverse()
        for i in l1:
            n1 = n1 + str(i)
        for i in l2:
            n2 = n2 + str(i)
        total = int(n1) + int(n2)
            
        return total
    
l1 = [2,4,3]
l2 = [5,6,4]

answer = Solution()

print(answer.addTwoNumbers(l1,l2))
