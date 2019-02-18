from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums:
            return []
        d = deque()
        res = []
        for i, v in enumerate(nums):
            # 构造单调递减序列，如果要插入的值大于 deque 中最后一个元素，将 deuqe 中最后一个元素删除
            while d and v >= nums[d[-1]]:
                d.pop()
            # 添加下标
            d.append(i)
            # 保证 deque 的长度不超过 k，比如 nums=[5, 4, 3, 2, 1]，deque 长度会超过 k
            if i - d[0] == k:
                d.popleft()
            # 如果 deque 中有超过 k 个，添加进 deque 中
            if i - k + 1 >= 0:
                res.append(nums[d[0]])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # nums = [1, -1]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
