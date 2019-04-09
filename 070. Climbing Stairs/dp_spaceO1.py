class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1
        if n < 2:
            return 1
        for i in range(2, n + 1):
            prev, cur = cur, prev + cur
        return cur


if __name__ == '__main__':
    n = 3
    print(Solution().climbStairs(n))
