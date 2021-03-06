# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        res = []
        for l in lists:
            while l:
                res.append((l.val, l))
                l = l.next
        res.sort(key=lambda t: t[0])
        dummy = ListNode(-1)
        pt = dummy
        for i in res:
            pt.next = i[1]
            pt = pt.next

        return dummy.next
