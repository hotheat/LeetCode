class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while len(bits) > 2:
            if bits[0] == 1:
                bits = bits[2:]
            elif bits[0] == 0:
                bits = bits[1:]
        return False if len(bits) == 0 else bits[0] == 0


bits = [1, 1, 1, 0]
bits = [1, 0, 0]
s = Solution()
print(s.isOneBitCharacter(bits))
