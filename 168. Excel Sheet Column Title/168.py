class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        代码错误，跑不出来
        """
        number = dict(zip(range(1, 27), [chr(i) for i in range(65, 91)]))

        number[0] = ''
        ans = ''

        # multi = 10
        # while n // 26 != 0:
        #     multi *= 10

        while True:
            div, mod = divmod(n, 26)
            if mod == 0:
                d, m = 26, 26
            else:
                d, m = div, mod
            print(d, m, div)
            if div == 0:
                ans += number[mod]
                break
            ans += number[d]
            n = mod
        return ans


n = 52
print(Solution().convertToTitle(n))
