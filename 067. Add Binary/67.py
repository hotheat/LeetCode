class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a), len(b))
        if len(a) < len(b):
            a, b = b, a
        b = b.zfill(l)
        ans = ''
        i, div, mod = 0, 0, 0
        while i < l:
            div, mod = divmod(int(a[l - i - 1]) + int(b[l - i - 1]) + div, 2)
            ans = str(mod) + ans
            i += 1
        return str(div) + ans if div == 1 else ans


a = "1010"
b = "1011"
print(Solution().addBinary(a, b))
