# https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays/
"""
只考虑两种情况:
1. 不交换 nums1[n-1] 和 nums2[n-1]
2. 交换 nums1[n-1] 和 nums2[n-1]

对于每种情况, 从 i=0 到 i=n-2, 一旦发现 任意nums[i] > nums[n-1],
就必须执行交换操作, 如果交换后依旧发现 任意nums[i] > nums[n-1], 返回 -1
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def slove(last1: int, last2: int) -> int:
            cnt = 0
            for x, y in zip(nums1, nums2):  # 简化代码, 因为两个不同数交换一定会满足下一条件, 但不会满足第二个条件, 简化了交换末尾元素的处理
                if x > last1 or y > last2:  # 第一个条件
                    if x > last2 or y > last1:  # 第二个条件
                        return inf
                    cnt += 1
            return cnt

        ans = min(slove(nums1[-1], nums2[-1]), slove(nums2[-1], nums1[-1]))
        return ans if ans < inf else -1
