from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in points:
            dst_cnt = defaultdict(int)
            for j in points:
                dst = (j[1] - i[1]) ** 2 + (j[0] - i[0]) ** 2
                dst_cnt[dst] += 1
            # 考虑采用顺序的排序组合 A_n^2
            for v in dst_cnt.values():
                ans += v * (v - 1)
        return ans


points = [[0, 0], [1, 0], [2, 0]]
print(Solution().numberOfBoomerangs(points))
