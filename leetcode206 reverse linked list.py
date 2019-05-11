# 单链表反转
# leetcode 206


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.prev = None
        
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head: return self.prev
        cur = ListNode(head.val) ## generate a dummy node called cur
        cur.next=self.prev
        head = head.next
        self.prev = cur        
        return self.reverseList(head)
