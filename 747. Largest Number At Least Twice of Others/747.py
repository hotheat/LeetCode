class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 储存最大值和索引及次大值和索引
        seqs = ((float('-inf'), -1), (float('-inf'), -1))
        ans = seqs[1][1]
        for i, v in enumerate(nums):
            if v > seqs[1][0]:
                seqs = (seqs[1], (v, i))
            elif v > seqs[0][0]:
                seqs = ((v, i), seqs[1])

        if seqs[1][0] >= seqs[0][0] * 2:
            ans = seqs[1][1]
        return ans


nums = [1, 2, 3, 4]
nums = [3, 6, 1, 0]
print(Solution().dominantIndex(nums))
