class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 最终结果不可能超过 len(num1) + len(num2) 的
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1) - 1, -1, -1):
                low = i + j + 1
                high = i + j
                mul = int(num2[i]) * int(num1[j])
                mul += res[low]
                res[low] = mul % 10
                res[high] += mul // 10

        i = 0
        while i < len(res):
            if res[i] != 0:
                break
            else:
                res.pop(0)

        final = ''.join([str(i) for i in res])
        return '0' if not final else final


if __name__ == '__main__':
    print(Solution().multiply('999', '999'))
