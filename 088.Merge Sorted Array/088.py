class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        输出: [1,2,2,3,5,6]
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        init_length = len(nums1)
        i, j = 0, 0
        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i + 1:i + 1 + m] = nums1[i: i + m]
                nums1[i] = nums2[j]
                i += 1
                j += 1
        sort_length = len(nums1)
        while sort_length > init_length:
            nums1.pop()
            init_length += 1
        while j < n:
            # 将剩余的 j 填充
            nums1[-(n - j)] = nums2[j]
            j += 1


s = Solution()
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
