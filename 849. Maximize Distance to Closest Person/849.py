class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dist = 0
        for i, cur in enumerate(seats):
            prev, behn = i, i
            if cur == 0:

                while prev >= 0 and seats[prev] == 0:
                    prev -= 1
                while behn < len(seats) and seats[behn] == 0:
                    behn += 1

                # 如果从当前位置到开头全是 0，看当前位置与后面最先遇到 1 的索引的位置
                if prev == -1 and behn - i > max_dist:
                    max_dist = behn - i
                # 如果从当前位置到结尾全是 0，看当前位置与前面最先遇到 1 的索引的位置
                elif behn == len(seats) and i - prev > max_dist:
                    max_dist = i - prev
                elif min(behn - i, i - prev) > max_dist:
                    max_dist = min(behn - i, i - prev)

        return max_dist


seats = [1, 0, 0, 0, 1, 0, 1]
# seats = [1, 0, 0, 0]
# seats = [0, 0, 0, 1]
# seats = [0, 1]
# seats = [1, 0]
print(Solution().maxDistToClosest(seats))
