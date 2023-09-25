# 2864. 最大二进制奇数  [https://leetcode.cn/problems/maximum-odd-binary-number/description/]
# 模拟题

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        one_n = s.count('1')
        if one_n == 1:
            return '0' * (n - 1) + '1'
        else:
            return '1' * (one_n - 1) + '0' * (n - one_n) + '1'
