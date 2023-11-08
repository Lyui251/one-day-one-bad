# 2924. 找到冠军 II https://leetcode.cn/problems/find-champion-ii/description/

"""
本质上是看是否只有一个入度为 0 的节点

对每个节点，判断它是否出现在 edges[i][1] 中。

如果恰好有一个节点没有出现，说明没有可以击败它的队伍，返回这个节点的编号。否则返回 −1。
"""


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * n

        for x, y in edges:
            deg[y] += 1

        ans = -1
        for i, d in enumerate(deg):
            if d == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
