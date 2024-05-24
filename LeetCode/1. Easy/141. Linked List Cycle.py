class Solution:
    def hasCycle(self, head) -> bool:
        glorb:set = set()
        while head:
            if head not in glorb:
                glorb.add(head)
                head = head.next
            else:
                return True

        return False