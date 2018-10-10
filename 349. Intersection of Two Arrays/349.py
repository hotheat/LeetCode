class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = {i: True for i in nums1}
        return list({i: 1 for i in nums2 if i in tmp}.keys())


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersection(nums1, nums2))
