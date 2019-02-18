import heapq


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        res = []
        if not nums:
            return res
        pq = MaxHeap(nums[:k])
        res.append(pq.pop())
        for i in range(k, len(nums)):
            pq.push(nums[i])
            res.append(pq.pop())
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # nums = [1, -1]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
