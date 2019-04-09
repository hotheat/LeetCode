from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        numberdict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        self.helper(digits, 0, '', numberdict, res)
        return res

    def helper(self, digits, index, cur, numberdict, res):
        if len(cur) == len(digits):
            res.append(cur)
            return

        for i in range(index, len(digits)):
            for j in numberdict[digits[i]]:
                self.helper(digits, i + 1, cur + j, numberdict, res)


if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))