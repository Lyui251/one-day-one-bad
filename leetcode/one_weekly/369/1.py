# https://leetcode.cn/problems/find-the-k-or-of-an-array/

"""
枚举 0 到 30 的每个比特位 i (因为 nums[i] < 2 ** 31)
遍历数组, 如果第 i 个比特位上的 1 的个数 >= k, 则把 2**i 加入答案中

如何统计第 i 个比特位上的 1 ?
=>   (x >> i) & 1 = 1

"""

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            cnt = sum(x >> i & 1 == 1 for x in nums)
            ans |= 1 << i if cnt >= k else 0
        return ans