from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [[1,0],[0,1]]
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if prerequisites == []:
            return True
        # 建邻接表, key: 先修课程，value: 后修课程
        adjacency_table = defaultdict(list)
        for i in prerequisites:
            adjacency_table[i[1]].append(i[0])
        # 记录每个节点的入度
        indegree = [0] * numCourses
        for i in prerequisites:
            indegree[i[0]] += 1

        # BFS，队列中记录入度为 0 的元素
        q = deque()
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)

        while len(q) > 0:
            allowed_course = q.popleft()
            for i in adjacency_table[allowed_course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        # 判断是否所有元素等于 0
        return all([i == 0 for i in indegree])


if __name__ == '__main__':
    pres = [
        [4, 1],
        [4, 2],
        [5, 2],
        [5, 3],
        [6, 4],
        [6, 5]
    ]
    nums = 7
    print(Solution().canFinish(nums, pres))
