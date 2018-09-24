from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 记录出现每个元素次数
        counts = Counter(nums)
        # 找出最大出现次数的元素
        maxc = max(counts.values())
        maxn = [k for k, v in counts.items() if v == maxc]

        inter = float('inf')
        for i in maxn:
            cnt, flag = 0, True
            for j, v in enumerate(nums):
                if v == i:
                    cnt += 1
                    # 记录最大出现次数元素的第一个坐标
                    if flag:
                        start = j
                        flag = False
                # 记录最大出现次数元素的最后一个坐标
                if cnt == maxc:
                    end = j
                    break
            # 取出坐标的最小值
            inter = min(inter, end - start + 1)
        return inter


# nums = [1, 2, 2, 3, 1]
nums = [1, 2, 2, 3, 1, 4, 2]
nums = [1, 1]
s = Solution()
print(s.findShortestSubArray(nums))
