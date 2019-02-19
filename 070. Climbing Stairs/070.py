class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        return self.dp(n, memo={1: 1, 2: 2})

    def dp(self, n, memo):
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)
            return memo[n]


if __name__ == '__main__':
    print(Solution().climbStairs(3))
