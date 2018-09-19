class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        def canPlaceFlowers(self, A, N):
            for i, x in enumerate(A):
                if (not x and (i == 0 or A[i - 1] == 0)
                        and (i == len(A) - 1 or A[i + 1] == 0)):
                    N -= 1
                    A[i] = 1
            return N <= 0
