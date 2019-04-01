import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        k = len(matrix) ** 2 - k + 1
        if len(matrix) == 0:
            return None

        min_heap = [float('-inf')] * k
        heapq.heapify(min_heap)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, matrix[i][j])
        return min_heap[0]


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(Solution().kthSmallest(matrix, k))
