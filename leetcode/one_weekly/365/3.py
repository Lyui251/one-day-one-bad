# 100076. 无限数组的最短子数组  [https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/description/]
#
# 除去 target 是 数组和 total 的倍数,
# 否则如果可以组合 target % total, 那么 一定就在 nums + nums 中的一段连续子数组中
#
# 举例:   nums = [1, 2, 3, 4], target = [1, 2, 3, 4] + [2, 3] = 15
#        那么 [2, 3] 或 [4, 1] 都是最短子数组
#        如果选 [2, 3], 那么答案可以是 [2, 3] + [4, 1, 2, 3]
#        如果选 [4, 1], 那么答案可以是 [4, 1] + [2, 3, 4, 1]
# 因此求 target % total, 如果 nums + nums 中得一段连续子数组可以组合出, 那么一定可以得出正确结果
#
# 因此可以使用 滑动窗口 来得到 nums + nums 中连续子数组的值得最短长度
from math import inf


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        left, n = 0, len(nums)
        s = 0
        ans = inf

        # 因为是 nums + nums, 因此 右边界right 要取到 n * 2
        for right in range(n * 2):
            s += nums[right % n]  # 记得取模运算
            while s > target % total:
                s -= nums[left % n]  # 记得取模运算
                left += 1

            if s == target % total:  # 因为 s 不一定每次移动的是 target % total
                ans = min(ans, right - left + 1)

        if ans == inf:  # 说明数组内无法组合
            return -1

        return ans + (target // total) * n
