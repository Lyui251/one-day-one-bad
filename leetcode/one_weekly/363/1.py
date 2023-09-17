#  100031. 计算 K 置位下标对应元素的和  ( https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/description/ )
#  有关集合论以及位运算:  https://leetcode.cn/circle/discuss/CaOJ45/

"""
按题意模拟

py关于 数字的二进制1的个数默认方法: x.bit_count()  3.10 以上版本

作为替代:
def bit_count(self):
    return bin(self).count("1")
"""

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i.bit_count() == k:
                ans += x
        return ans

