from typing import List
from collections import deque


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
        queue = deque([""])
        for i in digits:
            word = numberdict[i]
            qlen = len(queue)
            for j in range(qlen):
                popleft = queue.popleft()
                for k in word:
                    queue.append(popleft + k)

        return list(queue)


if __name__ == '__main__':
    digits = '2'
    print(Solution().letterCombinations(digits))
