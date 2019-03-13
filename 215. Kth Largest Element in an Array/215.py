from typing import List


class Solution:

    def partition(self, nums, low, high):
        pivot = nums[high]
        # j 的意义是 j 的左边都是比 pivot 大的数，右边都是比 pivot 小的数，是个临界位置
        j = low
        for i in range(low, high):
            # 大的放左边，小的放右边
            if nums[i] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            else:
                continue
        nums[high], nums[j] = nums[j], nums[high]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.find(nums, 0, len(nums) - 1, k)

    def find(self, nums, low, high, k):
        p = self.partition(nums, low, high)

        if k == p + 1:
            return nums[p]
        elif k > p + 1:
            return self.find(nums, p + 1, high, k)
        else:
            return self.find(nums, low, p - 1, k)


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(arr, k))
