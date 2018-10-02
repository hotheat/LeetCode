class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa, sb = sum(A), sum(B)
        bs = set(B)
        for i in A:
            if (sb - sa + 2 * i) / 2 in bs:
                return (i, int((sb - sa + 2 * i) / 2))


A = [1, 2, 5]
B = [2, 4]
print(Solution().fairCandySwap(A, B))
