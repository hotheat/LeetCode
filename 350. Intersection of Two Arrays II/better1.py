from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        print([[num] * min(c1[num], c2[num]) for num in c1 & c2])
        # return list((Counter(c1) & Counter(c2)).elements())
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])


nums1 = [1, 1, 2, 2]
nums2 = [1, 2, 2]
print(Solution().intersect(nums1, nums2))
