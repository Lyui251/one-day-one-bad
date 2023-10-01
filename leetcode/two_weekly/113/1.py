# 8039. 使数组成为递增数组的最少右移次数  ( https://leetcode.cn/problems/minimum-right-shifts-to-sort-the-array/ )

"""
O(n)
根据题意数组至多两段递增数组, 且nums[0] > nums[-1]

"""

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        i, n = 1, len(nums)
        while i < n and nums[i-1] < nums[i]:
            i += 1
        # 第一次遍历, nums已经是递增数组了
        if i == n:
            return 0
        # 如果不是递增数组且nums[0] <= nums[-1], 那么不满足题目条件
        if nums[0] <= nums[-1]:
            return -1

        st = i    # 第二段开始的位置
        i += 1
        while i < n and nums[i-1] < nums[i]:
            i += 1
        
        if i < n:    # 至少三段
            return -1
        return n - st
