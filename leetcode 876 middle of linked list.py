#leetcode 876 Middle of the Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        res = [head]
        while head.next:
            res.append(head.next)
            head = head.next
            i+=1
        if i%2==0:
            return res[i//2]
        else:
            return res[i//2+1]