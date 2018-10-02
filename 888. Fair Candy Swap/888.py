class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        exchanged = {}
        for i, va in enumerate(A):
            for j, vb in enumerate(B):
                if (i, j) not in exchanged:
                    if sum(A[:i] + [B[j]] + A[i + 1:]) == sum(B[:j] + [A[i]] + B[j + 1:]):
                        return [A[i], B[j]]
                exchanged[(A[i], B[j])] = True


A = [1, 2, 5]
B = [2, 4]
print(Solution().fairCandySwap(A, B))
