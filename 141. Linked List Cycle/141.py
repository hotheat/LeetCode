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
        slow, fast = head, head

        if fast is None: return False

        while fast.next:
            slow, fast = slow.next, fast.next
            if fast.next:
                fast = fast.next
            else:
                return False
            if slow == fast:
                return True
        return False
