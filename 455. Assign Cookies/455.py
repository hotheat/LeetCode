from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0

        g.sort()
        s.sort()
        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                g_idx += 1
                s_idx += 1
                res += 1
            else:
                s_idx += 1
        return res


if __name__ == '__main__':
    g, s = [1, 2, 3], [1, 1]
    # g, s = [1, 2, 3], [1, 2]
    print(Solution().findContentChildren(g, s))
