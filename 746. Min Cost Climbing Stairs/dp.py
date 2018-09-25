class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {0: 0, 1: 0}
        i = 2
        while i <= len(cost):
            memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
            i += 1
        return memo[len(cost)]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
print(s.minCostClimbingStairs(cost))
