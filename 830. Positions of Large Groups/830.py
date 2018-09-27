class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 1

        while j < len(S):
            if S[j] == S[i]:
                j += 1
            if j == len(S) or S[j] != S[i] :
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j

        return res


S = "aaa"
S = "abc"
S = "abbxxxxzzy"

print(Solution().largeGroupPositions(S))
