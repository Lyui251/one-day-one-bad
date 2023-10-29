#  https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

"""
把 0 看成 1, 设 s1, s2 为 nums1, nums2的元素和, 这是元素和的最小值

接下来进行分类讨论:

1. 如果 nums1 中有 0, nums2 中没有 0, 并且 s1 > s2, 那么 s2 无法增加, 返回 -1
2. 如果 nums2 中有 0, nums1 中没有 0, 并且 s1 < s2, 那么 s1 无法增加, 返回 -1
3. 如果 nums1 和 nums2 中都没有 0, 并且 s1 != s2, 那么无法相等, 返回 -1
4. 否则, 答案为 max(s1, s2)
"""
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(max(x, 1) for x in nums1)
        s2 = sum(max(x, 1) for x in nums2)
        z1 = 0 in nums1
        z2 = 0 in nums2

        if z1 and not z2 and s1 > s2 or \
           z2 and not z1 and s1 < s2 or \
           not z1 and not z2 and s1 != s2:
           return -1
        else:
            return max(s1, s2)