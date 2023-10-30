"""
1. 自顶向下
floor(x / 2) 是对 x 进行 向下取整除 2, 因此可以看成 右移操作
一个数 右移 多少次就会变成 0? 本题 n <= 10 ** 4, 在 13 次时是 1, 在 14 次时是 0

同时, 右移次数是可以叠加的, 因此我们可以记录子树中的节点右移了多少次.
所以可以定义 dfs(i, j) 表示 子树i 在 右移j次 的前提下, 最多可以得到的多大结果


进行两种操作, 因此用 [选或不选] 来思考, 是否要进行右移
1. 不右移: 答案为 (coins[i] >> j) - k + sum(dfs(child, j))
2. 右移:   答案为 (coins[i] >> (j+1)) + sum(dfs(child, j + 1))

结果取以上两种情况的最大值
"""
from functools import cache


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        # 建图
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 因为是无向图, 因此需要考虑遍历父节点的情况, 因此多一个变量 fa 记录 父节点
        @cache
        def dfs(i: int, j: int, fa: int) -> int:
            # 对当前节点进行操作1和操作2的结果
            res1, res2 = (coins[i] >> j) - k, coins[i] >> (j + 1)

            # 遍历子树
            for ch in g[i]:
                if ch != fa:
                    res1 += dfs(ch, j, i)
                    if j + 1 < 14:  # 13次右移内结果才会大于0, 14次及之后的结果为0因此无需计算
                        res2 += dfs(ch, j + 1, i)  # 选择右移, 因此后面节点右移次数要 加1

            return max(res1, res2)

        return dfs(0, 0, -1)  # 递归入口为 初始节点0, 进行右移次数0, 以及任意 不是节点0的子节点

