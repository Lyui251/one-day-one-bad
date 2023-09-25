"""
42. 接雨水
"""

"""
238. 除自身以外数组的乘积:  [https://leetcode.cn/problems/product-of-array-except-self/]
2256. 最小平均差:          [https://leetcode.cn/problems/minimum-average-difference/]
2483. 商店的最少代价:      [https://leetcode.cn/problems/minimum-penalty-for-a-shop/]


# 除 nums[i] 之外的其余元素的乘积, 可分为两部分 pre, sur;
# pre[i] 表示从 0 ~ i - 1 的元素处理后的数, sur[i] 表示从 i + 1 ~ n - 1 的元素处理后的数
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 时间 O(n)
        # 空间 O(1) 除去用来存储答案的 ans 数组, 各个变量均是常量
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = nums[-1]
        for i in range(n-2, -1, -1):
            ans[i] *= R
            R *= nums[i]
        
        return ans


        # 时间 O(n)
        # 空间 O(n)
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        sur = [1] * n
        for i in range(n-2, -1, -1):
            sur[i] = sur[i + 1] * nums[i + 1]
        
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i] * sur[i]
        # print(pre, sur)
        return ans
        





"""
2420. 找到所有好下标
"""

"""
2167. 移除所有载有违禁货物车厢所需的最少时间
"""

"""
2484. 统计回文子序列数目
"""

"""
2552. 统计上升四元组
"""

"""
2565. 最少得分子序列
"""
