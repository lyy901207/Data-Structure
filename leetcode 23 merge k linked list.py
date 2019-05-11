# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val>l2.val:
            temp = l2
            temp.next = self.mergeTwoLists(l1, l2.next)
            return temp
        else:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
            return temp
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        trv = 1
        
        while trv < k:
            for i in range(0, k - trv, trv * 2):
                #print('i:',i)
                lists[i] = self.mergeTwoLists(lists[i], lists[i + trv])
            trv *= 2
        return lists[0] if k > 0 else lists