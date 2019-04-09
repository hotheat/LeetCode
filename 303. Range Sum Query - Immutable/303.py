from typing import List
from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.accum = list(accumulate(nums))

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.accum[j]
        else:
            return self.accum[j] - self.accum[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
