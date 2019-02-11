# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        return self._merge_lists(lists, 0, len(lists) - 1)

    def _merge_lists(self, lists, low, high):
        if not lists:
            return None
        if low >= high:
            return lists[low]
        mid = (high - low) // 2 + low
        lefts = self._merge_lists(lists, low, mid)
        rights = self._merge_lists(lists, mid + 1, high)
        return self._merge(lefts, rights)

    def _merge(self, l1, l2):
        dummy = ListNode(-1)
        pt = dummy
        while l1 and l2:
            if l1.val < l2.val:
                pt.next = l1
                l1 = l1.next
            else:
                pt.next = l2
                l2 = l2.next
            pt = pt.next

        pt.next = l1 if not l2 else l2
        return dummy.next
