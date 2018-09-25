class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return self.dp(cost, len(cost), {0: 0, 1: 0})

    def dp(self, cost, index, memo):
        if index in memo:
            return memo[index]
        else:
            memo[index] = min(self.dp(cost, index - 1, memo) + cost[index - 1],
                              self.dp(cost, index - 2, memo) + cost[index - 2])
            return memo[index]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
print(s.minCostClimbingStairs(cost))
