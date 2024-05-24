class Solution:
    def isPalindrome(self, head) -> bool:
        glorb:list = []
        while head:
            glorb.append(head.val)
            head = head.next

        glarb:list = []
        for i in reversed(glorb):
            glarb.append(i)
        if glorb == glarb:
            return True
        else:
            return False