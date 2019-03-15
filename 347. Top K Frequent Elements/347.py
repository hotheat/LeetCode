from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = [(-float('inf'), None)] * k
        heapq.heapify(minheap)

        for i, v in count.items():
            if v > minheap[0][0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, (v, i))

        res = []
        for i in range(k):
            n = heapq.heappop(minheap)[1]
            res.append(n)
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
