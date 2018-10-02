class Solution(object):
    def maxDistToClosest(self, seats):
        # 用生成器存储有座位的坐标
        people = (i for i, seat in enumerate(seats) if seat)
        # 分别存储当前位置最近的左侧和右侧有座位的坐标
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:

                while future is not None and future < i:
                    # next 第二个参数是生成器耗尽后的返回值
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans


seats = [0, 1, 0, 0, 0, 1, 0, 1]
print(Solution().maxDistToClosest(seats))
