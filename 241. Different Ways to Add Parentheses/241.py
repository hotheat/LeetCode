from typing import List


class Solution:
    mem = {}

    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.ways(input)

    def ways(self, input):
        if input in Solution.mem:
            return Solution.mem[input]

        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                left = self.ways(input[:i])
                right = self.ways(input[i + 1:])
                # 得到的结果是笛卡尔积形式
                for j in left:
                    for k in right:
                        res.append(self.operat(j, k, input[i]))
        Solution.mem[input] = res
        return res

    def operat(self, j, k, op):
        if op == '+':
            return j + k
        elif op == '-':
            return j - k
        else:
            return j * k


if __name__ == '__main__':
    input = "2*3-4*5"
    input = "2"
    print(Solution().diffWaysToCompute(input))
