"""
类似把记忆化搜索翻译成递推的过程，我们也可以从下往上算：
"""


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        # 建图
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 自底向上, 返回对 coins[i] 进行 j 次右移操作结果 的数组
        def dfs(i: int, fa: int) -> list[int]:
            res1 = [0] * 14
            res2 = [0] * 14
            # 遍历子树
            for ch in g[i]:
                if ch == fa:    continue

                r = dfs(ch, i)
                for j in range(14):
                    res1[j] += r[j]
                    if j + 1 < 14:  # 13次右移内结果才会大于0, 14次及之后的结果为0因此无需计算
                        res2[j] += r[j + 1]  # 选择右移, 因此后面节点右移次数要 加1

            # 数组应返回得到的最大结果
            for j in range(14):                                         # 右移运算优先级低
                res1[j] = max(res1[j] + (coins[i] >> j) - k, res2[j] + (coins[i] >> (j + 1)))
            return res1

        return dfs(0, -1)[0]