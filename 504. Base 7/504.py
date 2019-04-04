class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = ''
        pnum = abs(num)
        while pnum != 0:
            pnum, mod = divmod(pnum, 7)
            res = str(mod) + res

        return res if num >= 0 else '-' + res


if __name__ == '__main__':
    num = 100
    num = 0
    num = -100
    print(Solution().convertToBase7(num))