import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        queue, res = [], []

        for l in lists:
            while l:
                heapq.heappush(queue, l.val)
                l = l.next

        while queue:
            res.append(heapq.heappop(queue))

        return res