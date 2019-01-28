class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tmp = []
        length = len(nums1) + len(nums2)
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        if i == len(nums1):
            tmp.extend(nums2[j:])
        else:
            tmp.extend(nums1[i:])
        print(tmp)
        if length % 2 == 0:
            return (tmp[length // 2 - 1] + tmp[length // 2]) / 2
        else:
            return tmp[length // 2]


if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    print(Solution().findMedianSortedArrays(nums1, nums2))
