class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        found = {}
        for i in nums:
            if i not in found:
                found[i] = True
            else:
                return True

        return False


arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
s = Solution()
print(s.containsDuplicate(arr))
