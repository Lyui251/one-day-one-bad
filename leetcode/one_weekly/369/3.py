# https://leetcode.cn/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 可以发现 f[i] 只与 f[i-1] 有关, 因此可以缩小为 三个常量 记录
        f0, f1, f2 = 0, 0, 0
        for i in range(n):
            chs = f0 + max(k - nums[i], 0)
            f0 = min(chs, f1)
            f1 = min(chs, f2)
            f2 = chs

        return f0

        # f = [[0] * 3 for _ in range(n + 1)]
        # for i in range(n):
        #     # chs = f[i-1][0] + max(k - nums[i], 0)   # 选
        #     chs = f[i][0] + max(k - nums[i], 0)   # 选

        #     f[i+1][0] = min(chs, f[i][1])
        #     f[i+1][1] = min(chs, f[i][2])
        #     f[i+1][2] = chs
        # return f[-1][0]

        # @cache
        # def dfs(i: int, j: int) -> int:
        #     """
        #     i 表示 nums 数组下标
        #     j 表示 nums[i] 右边没有选择增加的数字个数
        #     """
        #     if i < 0:
        #         return 0
        #     # 选
        #     res = dfs(i-1, 0) + max(k - nums[i], 0)
        #     # 不选, 不选的前提是 nums[i]的右边 不选的数字小于 2
        #     if j < 2:
        #         res = min(res, dfs(i-1, j+1))

        #     return res

        # return dfs(n-1, 0)
