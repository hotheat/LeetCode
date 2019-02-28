from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            lheight, rheight = height[left], height[right]
            area = max(area, min(lheight, rheight) * (right - left))
            if lheight < rheight:
                left += 1
            elif lheight > rheight:
                right -= 1
            else:
                left += 1
                right -= 1
        return area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
