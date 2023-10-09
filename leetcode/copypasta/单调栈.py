# LC 2334. 元素值大于变化阈值的子数组:  https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/
"""
提示 1
枚举每个元素，假设它是子数组中的最小值。
提示 2
子数组的左右边界最远能到哪？
提示 3
用单调栈来计算左右边界。

# 枚举 nums[i] 为连续子数组最小者, 用两个数组left, right 记录 最近左边, 右边比 nums[i] 小的数下标
# 此时 left[i]+1 是连续子数组的起点, right[i]-1 是连续子数组的终点
# 连续子数组长为 (right[i]-1) - (left[i] + 1) + 1 = right[i] - left[i] - 1
#
# 因此需要用单调栈记录下标, 当 nums[i] 小于等于 栈顶下标的元素时, 弹出栈顶元素
"""
class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        n = len(nums)

        left, st = [-1] * n, []
        for i, x in enumerate(nums):
            while st and x <= nums[st[-1]]:
                st.pop()
            if st:  left[i] = st[-1]
            st.append(i)

        right, st = [n] * n, []
        for i in range(n - 1, -1, -1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            if st:  right[i] = st[-1]
            st.append(i)

        for x, r, l in zip(nums, right, left):
            arr_len = r - l - 1
            if x > threshold / arr_len:
                return arr_len

        return -1
