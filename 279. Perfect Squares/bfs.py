from collections import deque


class Solution:
    def numSquares(self, n):
        """
        假设 n 由完全平方数构成的，构建一棵树，树的顶点是 n，每一层是减去不同完全平方数的值，
        目的是找出使差值等于 0 的最短路径，求树中的最短路径，可以考虑 BFS
        与按层遍历求树的深度思想类似
        https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
        :param n:
        :return:
        """
        if n < 2:
            return n

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        # value, level
        q = deque([(n, 0)])

        while len(q) > 0:
            value, l = q.popleft()
            for i in squares:
                if value < i:
                    break
                elif value - i > 0:
                    q.append((value - i, l + 1))
                else:
                    return l + 1


if __name__ == '__main__':
    print(Solution().numSquares(12))
