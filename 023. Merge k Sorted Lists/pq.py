from queue import PriorityQueue as PQueue
pq = PQueue()

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
                pq.put(l.val, l.val)
                l = l.next
        while not pq.empty():
            res.append(pq.get())
        return res

