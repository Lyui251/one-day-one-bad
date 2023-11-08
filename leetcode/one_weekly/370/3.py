# https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/description/
# 相似: 337. 打家劫舍 III: https://leetcode.cn/problems/house-robber-iii/description/
"""
正难则反，先把所有 values[i]加到答案中，然后考虑哪些 values[i] 不能选（撤销，不加入答案）。

设当前节点为 x，计算以 x 为根的子树是健康时，失去的最小分数。那么答案就是 values 的元素和，减去「以 0 为根的子树是健康时，失去的最小分数」

健康的子树只需要保持该条路径上一个点不为0
用 [选或不选] 进行分类讨论:

    1. 失去 values[x], 那么 x 的所有子孙节点都可以加入答案, 失去的最小分数就是 values[x]
    2. values[x] 加入答案, 问题变为[以 y 为根的子树是健康的, 失去的最小的分数], 此处的 y 是 x 的儿子.
       如果 x 有多个儿子, 累加失去的最小分数

这两种情况取最小值. 同时注意第一种情况不会继续向下递归, 所以当递归到叶子节点时, 叶子节点一定不能加入答案, 我们必须要返回 values[x].

代码实现时, 为了方便判断 x 是否为叶子节点, 可以假设还有一条 从0到-1 的边, 这样就不会把 根节点0 当作叶子.

"""


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        g[0].append(-1)  # 防特判, 根节点出发是一条链

        def dfs(i: int, fa: int) -> int:
            if len(g[i]) == 1:
                return values[i]

            # 选或不选
            res1, res2 = values[i], 0
            for son in g[i]:
                if son == fa:   continue
                res2 += dfs(son, i)

            return min(res1, res2)

        return sum(values) - dfs(0, -1)
