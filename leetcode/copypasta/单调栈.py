# LC 2454. 下一个更大元素 IV:  https://leetcode.cn/problems/next-greater-element-iv/description/ 2175
"""
从左向右遍历 nums, 用(递减)单调栈 s 记录元素, 如果 x=nums[i] 比 s 的栈顶大,
则 x 是栈顶的下个更大元素, 弹出栈顶. 最后把 x 入栈(实际入栈的是下标 i)

把弹出的元素加到另一个栈 t 中(注意保持原始顺序), 后续循环时, 如果 y=nums[j] 比 t 的栈顶大
则 y 是栈顶的下下个更大元素, 记录答案, 弹出栈顶
"""
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        s, t = [], []

        ans = [-1] * len(nums)
        for i, x in enumerate(nums):
            # 当 x 大于 t 栈顶的下标对应数时, 说明 x 是 nums[t[-1]] 的第二大整数
            while t and x > nums[t[-1]]:
                ans[t.pop()] = x

            # 如果倒序遍历, 那么会反转原本的顺序,
            # 比如 [12, 0, 12], 在遇见第二个 12 时, s = [0 (12), 1 (0)], 如果选择 pop(),
            # 那么 t = [1 (0), 0 (12)], 本应得到 t = [0, 1],
            # 因此需要通过变量 j, 得到需要删除的长度, 然后通过切片得到正确的顺序
            j = len(s) - 1
            while j >= 0 and s and x > nums[s[j]]:
                j -= 1
            # t 记录 nums 右端有一个大于的整数的 数下标
            t += s[j + 1:]
            del s[j + 1:]  # 需要从 s 中删除的下标们
            s.append(i)

        return ans


# LC 2334. 元素值大于变化阈值的子数组:  https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/ 2381
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
