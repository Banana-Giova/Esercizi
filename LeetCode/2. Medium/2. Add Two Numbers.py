class Solution:
    def addTwoNumbers(self, l1: list, 
                      l2: list) -> list[int]:
        
        """
        while head:
        glorb.append(head.val)
        head = head.next
        """

        list(str(l1))
        list(str(l2))
        l1.reverse()
        l2.reverse()

        l1_str:str = ''
        for i in l1:
            l1_str += str(i)
        l2_str:str = ''
        for i in l2:
            l2_str += str(i)
        
        l3 = list(str(int(l1_str) + int(l2_str)))
        l3.reverse()
        return l3
    
solution:Solution = Solution()
print(solution.addTwoNumbers([2,4,3], [5,6,4]))