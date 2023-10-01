# 100086. 有序三元组中的最大值 II   [https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/]
#
# 方法一: 枚举 j
# 枚举 j，为了让 (nums[i]−nums[j]) *∗nums[k] 尽量大，我们需要知道 j 左侧元素的最大值，和 j 右侧元素的最大值。
# 也就是 nums 的前缀最大值 preMax 和后缀最大值 sufMax，这都可以用递推预处理出来：
#
# preMax[i]=max(preMax[i−1],nums[i])
# sufMax[i]=max(sufMax[i+1],nums[i])
# 代码实现时，可以只预处理 sufMax 数组，preMax 可以在计算答案的同时算出来。


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        surMax = [0] * (n + 1)
        for k in range(n - 1, -1, -1):
            surMax[k] = max(surMax[k + 1], nums[k])

        preMax = 0
        ans = 0
        for j in range(n):
            ans = max(ans, (preMax - nums[j]) * surMax[j + 1])
            preMax = max(preMax, nums[j])

        return ans

