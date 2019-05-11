# leetcode 141 linked list cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        
        return False
            