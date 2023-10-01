# 8038. 收集元素的最少操作次数 [https://leetcode.cn/problems/minimum-operations-to-collect-elements/description/]


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mask, target = 0, (1 << (k + 1)) - 2
        n = len(nums)
        for i in range(n-1, -1, -1):
            mask |= 1 << nums[i]
            if mask & target == target:
                return n - i