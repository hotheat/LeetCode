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
                res.append(l.val)
                l = l.next
        return sorted(res)
