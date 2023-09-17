#  100040. 让所有学生保持开心的分组方法数  ( https://leetcode.cn/problems/happy-students/description/ )

"""
比大小 -> 排序

为什么排序?   

1.  这位学生被选中, 并且被选中的学生人数严格大于 nums[i]
    意味着 nums[i] 越小, 越能够满足这个条件
2.  这位学生没有被选中, 并且被选中的学生人数严格小于 nums[i]
    意味着 nums[i] 越大, 越能够满足这个条件
3.  结论: 在选择学生时, 应当优先选择 nums[i] 小的学生
4.  排序后, 数组的前缀是优先要选的
5.  只要判断:
      1. (选中的学生人数)i + 1 > nums[i]
      2. (选中的学生人数)i + 1 < nums[i + 1]
"""


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] > 0   # 可以一个都不选

        for i in range(n - 2):
            if nums[i] < i + 1 < nums[i + 1]:
                ans += 1
                
        # 题目中一定可以都选, 否则 return ans + 1 if n > nums[-1] else 0
        return ans + 1  
